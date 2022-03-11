import numpy as np

from torch import eq, tensor
from config.Config import BasicSetting, PrivateSetting
from config.ConfigEvaluation import EvaluationPara


def show_total_acc(mode:str, total:int, totalCorrect:int):
    """
    Show overall accuracy for each epoch in terminal.

    Args:
        mode: title show in terminal
        total: total data amount
        totalCorrect: correctly predicted data amount
    """
    if EvaluationPara.showAcc:
        print('{} acc: {:.4f} %'.format(mode, 100 * totalCorrect / total))
    

def show_class_acc(classTotal:list, classCorrect:list, className:list):
    """
    Show accuracy of each class in terminal.

    Args:
        classTotal: data amount of each class
        classCorrect: correctly predicted data amount of each class
        className: class name of each class
    """
    for i, cls in enumerate(className):
        if classCorrect[i] == 0 and classTotal[i] == 0:
            classTotal[i] = 1
        print('- Accuracy of class {} : {:.4f} %'.format(cls, 100 * classCorrect[i] / classTotal[i]))


def show_num_data(classTotal:list, classCorrect:list):
    """
    Show data amount and correctly predicted amount of each class in terminal.

    Args:
        classTotal: data amount of each class
        classCorrect: correctly predicted data amount of each class
    """
    print("Total data for each class : ", classTotal)
    print("Correct data for each class: ", classCorrect)


def show_rate(total, totalCorrect, classTotal, classCorrect, cfMatrix, targetIndex):
    """
    Show leakage, overkill, defectAcc in terminal.

    Args:
        total: total data amount
        totalCorrect: correctly predicted data amount
        classTotal: data amount of each class
        classCorrect: correctly predicted data amount of each class
        cfMatrix: confusion matrix
        targetIndex: the class index of "OK" or "Pass" in the className list 
    """
    leakage = (sum(row[targetIndex] for row in cfMatrix) - cfMatrix[targetIndex][targetIndex]) / (total - classTotal[targetIndex]) * 100
    overkill = 100 - (100 * classCorrect[targetIndex] / classTotal[targetIndex])
    defectAcc = (totalCorrect - classCorrect[targetIndex]) / (total - classTotal[targetIndex]) * 100
    print("leakage: {:.4f}%, overkill: {:.4f}%, defectAcc: {:.4f}%".format(leakage, overkill, defectAcc))


def show_wrong_file(nameList, predict:tensor, labels:tensor, confidence:tensor, className, count:int):
    """
    Show the file names of incorrectly predict datas.

    Args:
        nameList: list include all file names
        predict: model prediction (dtype: tensor)
        labels: correct label (dtype:tensor)
        confidence: predicted confidence
        className: class name of each class
        count: use to record current file
    """
    if EvaluationPara.showWrongFile:
        confid = confidence.cpu().numpy()
        confid = confid[:, :len(className)]
        for i in range(len(predict)):
            fullname = nameList[count]
            count += 1
            if not eq(predict[i], labels[i]):
                print("Wrong file: {}, Label: {}, Pred: {}".format(fullname, className[int(labels[i])], className[int(predict[i])]))
                print("Confid: {}\n".format(confid[i])) 
        return count
