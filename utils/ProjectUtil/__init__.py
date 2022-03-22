# -*- coding: utf-8 -*-

"""
Created on FRI MAR 4 17:00:00 2021
@author: ShanYang
"""

import json, jwt, os, shutil
from pkgutil import get_data
from datetime import datetime

key = 'auo'
algorithm = 'HS256'
rootProjectPath = f"./projects"

def decode_key(token):
    try:
        deDict = jwt.decode(token, key, algorithms=[algorithm])
        return True, deDict
    except:
        return False, "Decode key failed"

def get_projects():
    try:
        return True, os.listdir(rootProjectPath)
    except:
        return False, "Get projects failed"

def create_project(projectName):
    try:
        projectPath = f"{rootProjectPath}/{projectName}"
        if os.path.isdir(projectPath):
            return False, "Project already exists"
        os.makedirs(f"{projectPath}/experiments")
        os.makedirs(f"{projectPath}/runs")
        projectList = os.listdir(rootProjectPath)
        return True, projectList
    except:
        return False, "Create project failed"

def save_config_as_json(projectName, config):
    try:
        jsonName = datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f"{rootProjectPath}/{projectName}/experiments/{jsonName}.json", 'w') as jsonFile:
            json.dump(config, jsonFile, indent=4)
        return True, f"{rootProjectPath}/{projectName}/experiments/{jsonName}.json"
    except:
        return False, "Save config failed"

def find_project(projectName):
    try:
        projectPath = f"{rootProjectPath}/{projectName}"
        if os.path.isdir(projectPath):
            return True, projectPath
        else:
            return False, "Project doesn't exist"
    except:
        return False, "Find project failed"

def get_config(projectPath):
    try:
        configList = os.listdir(f"{projectPath}/experiments")
        configDict = {}
        for configFile in configList:
            with open(f"{projectPath}/experiments/{configFile}") as jsonFile:
                config = json.load(jsonFile)
                configDict[str(configFile.split('.')[0])] = config
        return True, configDict
    except:
        return False, "Get config failed"

def set_config_dataset(projectPath, experimentId, datasetPath):
    try:
        configPath = f"{projectPath}/experiments/{experimentId}.json"
        if not os.path.isfile(configPath):
            return False, "Experiment not found"

        datasets = get_datasets(projectPath)
        if not datasets or not datasetPath in datasets:
            return False, "Dataset not found"

        config = None
        with open(configPath, 'r') as fin:
            config = json.load(fin)
        if not config:
            return False, "Load config failed"

        config['Config']['PrivateSetting']['datasetPath'] = datasetPath
        with open(configPath, 'w') as fout:
            json.dump(config, fout, indent=4)
        return True, config
    except Exception as err:
        print(err)
        return False, err

def check_data_uploaded(datasetPath):
    try:
        if not os.path.isdir(datasetPath):
            return False, "There is no folder"
        dataList = os.listdir(datasetPath)
        if not dataList:
            return False, "There is no data"
        return True, dataList
    except:
        return False, "Check data uploaded failed"

def check_data_split(datasetPath):
    try:
        isTrain = isValid = isTest = 0
        datasetList = []
        dataList = os.listdir(datasetPath)
        for data in dataList:
            if os.path.isdir(f"{datasetPath}/{data}"):
                if data == "Train":
                    isTrain = 1
                    datasetList.append(data)
                elif data == "Valid":
                    isValid = 1
                    datasetList.append(data)
                elif data == "Test":
                    isTest = 1
                    datasetList.append(data)
        if isTrain == 1 and isValid == 1 and isTest == 1:
            return True, datasetList
        return False, "Please set Train/ Valid/ Test"
    except:
        return False, "Check data split failed"

def check_data_labeled(datasetPath):
    try:
        classList = []
        dataList = os.listdir(datasetPath)
        for data in dataList:
            if os.path.isdir(f"{datasetPath}/{data}"):
                if check_class_name_legal(data): 
                    classList.append(data)
        if not classList:
            return False, "There is no classify"
        return True, classList
    except:
        return False, "Check data labeled failed"

def check_class_name_legal(className):
    try:
        illegalName = ["train", "training", "val", "valid", "validation",
                    "test", "testing", "inference", "inf"]
        if illegalName.index(className.lower()):
            return False
    except:
        return True

def get_datasets(projectPath):
    try:
        datasets = {}
        datasetFilePath = f"{projectPath}/datasets.json"
        if os.path.exists(datasetFilePath):
            with open(f"{projectPath}/datasets.json", 'r') as fin:
                datasets = json.load(fin)
        return datasets
    except Exception as err:
        print(err)

def remove_dataset(projectPath, datasetPath):
    try:
        datasets = {}
        datasetFilePath = f"{projectPath}/datasets.json"
        if os.path.exists(datasetFilePath):
            with open(f"{projectPath}/datasets.json", 'r') as fin:
                datasets = json.load(fin)
        if datasetPath in datasets:
            del datasets[datasetPath]
            with open(f"{projectPath}/datasets.json", 'w') as fout:
                json.dump(datasets, fout, indent=4)
        return datasets
    except Exception as err:
        print(err)

def add_dataset(projectPath, datasetPath, uploaded=False, labeled=False, split=False):
    try:
        datasets = {}
        datasetFilePath = f"{projectPath}/datasets.json"
        if os.path.exists(datasetFilePath):
            with open(f"{projectPath}/datasets.json", 'r') as fin:
                datasets = json.load(fin)
        
        datasets[datasetPath] = {
            'uploaded': uploaded,
            'labeled': labeled,
            'split': split,
        }

        with open(f"{projectPath}/datasets.json", 'w') as fout:
            json.dump(datasets, fout, indent=4)
    except Exception as err:
        print(err)

def save_in_run_queue(projectName, experimentId, task):
    '''
    save a run process in run queue
    '''
    try:
        projectPath = f"{rootProjectPath}/{projectName}"
        runId = create_run(projectPath, experimentId)
        if not runId:
            return False, "create run failed"

        runQueueJsonPath = f"main/run_queue.json"
        if os.path.exists(runQueueJsonPath):
            with open(runQueueJsonPath, 'r') as queueFile:
                queueDict = json.load(queueFile)
            queue = queueDict["queue"]
            newRun = {
                "projectName": projectName,
                "experimentId": experimentId,
                "runId": runId,
                "task": task
            }
            queue.append(newRun)
            queueDict = {"queue": queue}
            with open(runQueueJsonPath, 'w') as queueFile:
                json.dump(queueDict, queueFile, indent = 4)

    except Exception as err:
        print(err)
        return False

def create_run(projectPath, experimentId):
    """
    1. create run folder
    2. copy exp config to run
    """
    try:
        runName = datetime.now().strftime('%Y%m%d%H%M%S')
        runPath = f"{projectPath}/runs/{runName}"
        if os.path.isdir(runPath):
            return False
        os.makedirs(runPath)
        experimentConfigPath = f"{projectPath}/experiments/{experimentId}.json"
        runConfigPath = f"{runPath}/{runName}.json"
        shutil.copy(experimentConfigPath, runConfigPath)
        return runName
    except:
        return None