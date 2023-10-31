from qiniu import Auth
import qiniu.config

import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

Access_Key = 'Access_Key'
Secret_Key = 'Secret_Key'

# 构建鉴权对象
query = Auth(Access_Key, Secret_Key)

# 确定上传的空间
Bucket_Name = 'Bucket_Name'

# 准备保存的文件名
File_Name = 'File_Name'

# 视频自动化处理队列
PipeLine = 'PipeLine'
