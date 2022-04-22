import os, csv, json
from torch import tensor
from config.Config import BasicSetting, PrivateSetting
from config.ConfigResultStorage import ResultStorage


def save_epoch_acc_txt(epoch:int, total:int, totalCorrect:int, classTotal:list, classCorrect:list, className:list):
    """
    Save epoch accuracy and class accuracy into txt file.

    Args:
        epoch: current epoch number
        total: total data amount
        totalCorrect: correctly predicted data amount
        classTotal: data amount of each class
        classCorrect: correctly predicted data amount of each class
        className: list of class name
    Return:
        ValidAcc.txt
    """
    if ResultStorage.saveAccTxt["switch"]:
        if epoch == 0:
            with open(f'./{PrivateSetting.outputPath}/ValidAcc.txt','w') as fAcc:
                print('Validation acc of epoch {}: {:.4f} %'.format(epoch+1, 100 * totalCorrect / total), file = fAcc)
                for i, cls in enumerate(className):
                    print('- Accuracy of class {:.5s} : {:.4f} %'.format(cls, 100 * classCorrect[i] / classTotal[i]), file = fAcc)
        else:
            with open(f'./{PrivateSetting.outputPath}/ValidAcc.txt','a') as fAcc:
                print('\nValidation acc of epoch {}: {:.4f} %'.format(epoch+1, 100 * totalCorrect / total), file = fAcc)
                for i, cls in enumerate(className):
                    print('- Accuracy of class {:.5s} : {:.4f} %'.format(cls, 100 * classCorrect[i] / classTotal[i]), file = fAcc)


def save_epoch_acc_json(epoch:int, totalEpoch: int, total:int, totalCorrect:int):
    """
    Save epoch accuracy and class accuracy into json file.

    Args:
        epoch: current epoch number
        totalEpoch: total epoch number
        total: total data amount
        totalCorrect: correctly predicted data amount
        classTotal: data amount of each class
        classCorrect: correctly predicted data amount of each class
        className: list of class name
    Return:
        modelTraining.json
    """
    jsonFilePath = f'./{PrivateSetting.outputPath}/modelTraining.json'
    epochDict = {
        "model": {
            "epoch": epoch + 1,
            "total": totalEpoch
        },
        "valid": {
            "accuracy": totalCorrect / total
        }
    }
    infoDict = {}
    if epoch != 0:
        if os.path.exists(jsonFilePath):
            with open(jsonFilePath, 'r') as fAcc:
                infoDict = json.load(fAcc)
    infoDict[str(epoch + 1)] = epochDict
    with open(jsonFilePath, 'w') as fAcc:
        json.dump(infoDict, fAcc, indent=4)


def output_result_csv(nameList:list, predict:tensor, labels:tensor, confidence:tensor, className:list, count:int, mode=BasicSetting.task):
    """
    Output test result into csv file, file name : Test_result.csv or Inference_result.csv.

    Args:
        nameList: list include all file names
        predict: model prediction (dtype: tensor)
        labels: correct label (dtype:tensor)
        confidence: predicted confidence
        className: class name of each class
        count: use to record current file

    format in csv file: 
        Filename | Ground truth | Prediction | Confidence of each class

    """
    ### Create csv file and title
    if mode == "Test":
        fileName = 'Test_result.csv'
        title = ['Filename', 'Ground truth', 'Prediction']
    elif mode =="Inference":
        fileName = 'Inference_result.csv'
        title = ['Filename', 'Prediction']
    if count == 0 :
        with open(os.path.join(PrivateSetting.outputPath, fileName), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            title.extend(className)
            writer.writerow(title)
            csvfile.close()

    ### Write result to csv file
    confidence = confidence.tolist()
    for i in range(len(predict)):
        fullname = nameList[count]
        with open(os.path.join(PrivateSetting.outputPath, fileName), 'a', newline='') as csvfile:
            if mode == "Test":
                result = [fullname, className[int(labels[i])], className[int(predict[i])]]
            elif mode == "Inference":
                result = [fullname, className[int(predict[i])]]
            result.extend(confidence[i][:len(className)])
            writer = csv.writer(csvfile)
            writer.writerow(result)
        count += 1
    return count