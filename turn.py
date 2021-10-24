# coding=UTF-8
import os
import subprocess

def ffmpeg_Video(VideoPath):
    # 提取视频路径下所有文件名
    for filepath, dirnames, filenames in os.walk(VideoPath):
        if " " in filepath:
            filepath = str(filepath).replace(" ", '')
        for filename in filenames:
            if " " in filename:
                filename = str(filename).replace(" ", '')
            print(filename)
            input = os.path.join(filepath, filename)
            for x in turn:
                if x in input:
                    output = str(input).replace(x, '.mp4')
                    # 提取视频中的音频信息
                    strcmd = r"D:\githubrepo\PythonScript\转换MP4\ffmpeg\bin\ffmpeg.exe -i " + input + " " + output
                    subprocess.call(strcmd, shell=True)
                    os.remove(input)

turn = ['.mkv','.rmvb']
VideoPath = r'D:\ForTv'
ffmpeg_Video(VideoPath)
