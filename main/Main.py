from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import ProjectUtil

def response(code, message, data=None):
    # code=0 for success, code=1 for fail
    return {'code': code, 'message': message, 'data': data}

app = Flask(__name__)
CORS(app)

@app.route('/create-project-by-key', methods=['POST'])
def create_project_by_key():
    '''
    decode key to get config
    create a new project folder/ or already existed
    save config as json

    {
        "name": "aaaa",
        "key": "# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb25maWcuZGF0YXNldFBhdGgiOiIiLCJDb25maWdQcmVwcm9jZXNzLlByZXByb2Nlc3NQYXJhLmltYWdlU2l6ZSI6WzIyNCwyMjRdLCJDb25maWdQcmVwcm9jZXNzLlByZXByb2Nlc3NQYXJhLm5vcm1hbGl6ZSI6eyJzd2l0Y2giOjEsIm1vZGUiOjQsIm1lYW4iOlswLjQ5MDAyOTI5LDAuNDkwMDI5MjksMC40OTAwMjkyOV0sInN0ZCI6WzAuMjYxODQ2MTMsMC4yNjE4NDYxMywwLjI2MTg0NjEzXX0sIkNvbmZpZ1ByZXByb2Nlc3MuUHJlcHJvY2Vzc1BhcmEuYnJpZ2h0bmVzcyI6MCwiQ29uZmlnUHJlcHJvY2Vzcy5QcmVwcm9jZXNzUGFyYS5ibHVyIjowLCJDb25maWdQcmVwcm9jZXNzLlByZXByb2Nlc3NQYXJhLmN1dG1peCI6MCwiQ29uZmlnUHJlcHJvY2Vzcy5QcmVwcm9jZXNzUGFyYS5tb3NhaWMiOjAsIkNvbmZpZ0F1Z21lbnRhdGlvbi5BdWdtZW50YXRpb25QYXJhLnJhbmRvbUhvcml6b250YWxGbGlwIjp7InN3aXRjaCI6MSwicHJvYmFiaWxpdHkiOjAuNX0sIkNvbmZpZ0F1Z21lbnRhdGlvbi5BdWdtZW50YXRpb25QYXJhLnJhbmRvbVZlcnRpY2FsRmxpcCI6eyJzd2l0Y2giOjAsInByb2JhYmlsaXR5IjowLjV9LCJDb25maWdNb2RlbFNlcnZpY2UuTG9zc0Z1bmN0aW9uUGFyYS5sb3NzRnVuY3Rpb24iOiJDcm9zc0VudHJvcHlMb3NzIiwiQ29uZmlnTW9kZWxTZXJ2aWNlLkxlYXJuaW5nUmF0ZS5sZWFybmluZ1JhdGUiOjAuMDEsIkNvbmZpZ01vZGVsU2VydmljZS5PcHRpbWl6ZXJQYXJhLlNHRCI6eyJzd2l0Y2giOjAsIm1vbWVudHVtIjowLjksImRhbXBlbmluZyI6MCwid2VpZ2h0RGVjYXkiOjAuMDAwNSwibmVzdGVyb3YiOjB9LCJDb25maWdNb2RlbFNlcnZpY2UuT3B0aW1pemVyUGFyYS5BZGFtIjp7InN3aXRjaCI6MSwiYmV0YXMiOlswLjksMC45OTldLCJlcHMiOjFlLTgsIndlaWdodERlY2F5IjowLjAwMDUsImFtc2dyYWQiOjB9LCJDb25maWdNb2RlbFNlcnZpY2UuT3B0aW1pemVyUGFyYS5BZGFkZWx0YSI6eyJzd2l0Y2giOjAsInJobyI6MC45LCJlcHMiOjAuMDAwMDAxLCJ3ZWlnaHREZWNheSI6MH0sIkNvbmZpZ01vZGVsU2VydmljZS5PcHRpbWl6ZXJQYXJhLkFkYW1XIjp7InN3aXRjaCI6MCwiYmV0YXMiOlswLjksMC45OTldLCJlcHMiOjFlLTgsIndlaWdodERlY2F5IjowLjAxLCJhbXNncmFkIjowfSwiQ29uZmlnTW9kZWxTZXJ2aWNlLk9wdGltaXplclBhcmEuTkFkYW0iOnsic3dpdGNoIjowLCJiZXRhcyI6WzAuOSwwLjk5OV0sImVwcyI6MWUtOCwid2VpZ2h0RGVjYXkiOjAsIm1vbWVudHVtRGVjYXkiOjAuMDA0fSwiQ29uZmlnTW9kZWxTZXJ2aWNlLlNjaGVkdWxlclBhcmEuc3RlcExSIjp7InN3aXRjaCI6MSwic3RlcF9zaXplIjoxLCJnYW1tYSI6MC41fSwiQ29uZmlnTW9kZWxTZXJ2aWNlLlNjaGVkdWxlclBhcmEuY29zaW5lQW5uZWFsaW5nTFIiOnsic3dpdGNoIjowLCJldGFfbWluIjowfSwiQ29uZmlnUHl0b3JjaE1vZGVsLlNlbGVjdGVkTW9kZWwubW9kZWwiOnsic3RydWN0dXJlIjoicmVnbmV0X3lfNDAwbWYiLCJwcmV0cmFpbmVkIjoxfSwiQ29uZmlnUHl0b3JjaE1vZGVsLkNsc01vZGVsUGFyYS5jdWRhRGV2aWNlIjoxLCJDb25maWdQeXRvcmNoTW9kZWwuQ2xzTW9kZWxQYXJhLmJhdGNoU2l6ZSI6OCwiQ29uZmlnUHl0b3JjaE1vZGVsLkNsc01vZGVsUGFyYS5lcG9jaHMiOjIsIkNvbmZpZ1Bvc3Rwcm9jZXNzLlBvc3RQcm9jZXNzUGFyYS5jb25maWRlbmNlRmlsdGVyIjp7InN3aXRjaCI6MSwidGhyZXNob2xkIjowLjgsInNlbGVjdExhYmVsIjoiT0siLCJjbGFzc0xpc3QiOlsiQVUwMiIsIkVOMDEiLCJFTjAyIiwiRU4wMyIsIklUNDMiLCJPSyIsIlNNMDAuT1QwOCIsIlNNMDMuU00wNyIsIlNNMDQiLCJTTTA1Il19LCJDb25maWdFdmFsdWF0aW9uLkV2YWx1YXRpb25QYXJhLnNob3dBY2MiOjEsIkNvbmZpZ0V2YWx1YXRpb24uRXZhbHVhdGlvblBhcmEuc2hvd0NsYXNzQWNjIjoxLCJDb25maWdFdmFsdWF0aW9uLkV2YWx1YXRpb25QYXJhLnNob3dOdW1PZkNsYXNzZXMiOjAsIkNvbmZpZ0V2YWx1YXRpb24uRXZhbHVhdGlvblBhcmEuc2hvd1JhdGUiOnsic3dpdGNoIjoxLCJ0YXJnZXRJbmRleCI6Ik9LIn0sIkNvbmZpZ0V2YWx1YXRpb24uRXZhbHVhdGlvblBhcmEuc2hvd1dyb25nRmlsZSI6MCwiQ29uZmlnUmVzdWx0U3RvcmFnZS5SZXN1bHRTdG9yYWdlLnNhdmVGaW5hbFdlaWdodCI6MCwiQ29uZmlnUmVzdWx0U3RvcmFnZS5SZXN1bHRTdG9yYWdlLnNhdmVDaGVja3BvaW50Ijp7InN3aXRjaCI6MCwic2F2ZUl0ZXIiOjF9LCJDb25maWdSZXN1bHRTdG9yYWdlLlJlc3VsdFN0b3JhZ2Uuc2F2ZUFjY1R4dCI6MSwiQ29uZmlnUmVzdWx0U3RvcmFnZS5SZXN1bHRTdG9yYWdlLmRyYXdBY2NDdXJ2ZSI6MSwiQ29uZmlnUmVzdWx0U3RvcmFnZS5SZXN1bHRTdG9yYWdlLmRyYXdDb25mdXNpb25NYXRyaXgiOjF9.utwO6RVjPzR47YP8bbjeij4CJTDHM0Oe8WyG3tgwgkY"
    }
    '''
    data = request.get_json()
    if not data:
        return response(1, "There is no data.")

    key = data['key']
    ok, config = ProjectUtil.decode_key(data['key'])
    if not ok:
        return response(1, config)

    projectName = data['name']
    ok, projectList = ProjectUtil.create_project(projectName)
    if not ok:
        return response(1, projectList)

    ok, configPath = ProjectUtil.save_config_as_json(projectName, config)
    if not ok:
        return response(1, configPath)
    
    return response(0, "success", {"projects": projectList})

@app.route('/get-experiments', methods=['POST'])
def get_experiments():
    '''
    return experiment config
    '''
    data = request.get_json()
    if not data:
        return response(1, "There is no data.")
    
    projectName = data['name']
    ok, projectPath = ProjectUtil.find_project(projectName)
    if not ok:
        return response(1, projectPath)

    ok, config = ProjectUtil.get_config(projectPath)
    if not ok:
        return response(1, config)

    return response(0, "success", config)


@app.route('/check-dataset', methods=['POST'])
def check_dataset():
    '''
    check dataset status: {uploaded: bool, labeled: bool, split: bool}
    '''
    data = request.get_json()
    if not data:
        return response(1, "There is no data.")

    uploaded = labeled = split = False
    
    datasetPath = data['datasetPath']
    ok, dataList = ProjectUtil.check_data_uploaded(datasetPath)
    if not ok:
        return response(1, dataList)
    uploaded = True

    ok, classList = ProjectUtil.check_data_labeled(datasetPath)
    if not ok:
        return response(0, "success", {"uploaded": uploaded, "labeled": labeled, "split": split})
    labeled = True

    ok, datasetList = ProjectUtil.check_data_split(datasetPath)
    if not ok:
        return response(0, "success", {"uploaded": uploaded, "labeled": labeled, "split": split})
    labeled = True

    
    return response(0, "success", {"uploaded": uploaded, "labeled": labeled, "split": split})

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()