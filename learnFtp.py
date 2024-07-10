from paramiko import SSHClient
import paramiko
from scp import SCPClient
ROOT = '/home/ftp_wobba/race_data'
ROOT_LOCAL = r'C:\Users\rreyn\Desktop\python1\ACC\data\\'

ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("redacted", port=redacted, username="redacted", password="redacted")

#scp = SCPClient(ssh.get_transport())
#scp.get

sftp = ssh.open_sftp()
sftp.chdir(ROOT)
#print(sftp.getcwd())
#print(sftp.listdir())

for dir in sftp.listdir():
    print(f'scanning: {dir}')
    sftp.chdir(f'{ROOT}/{dir}')
    if 'results' in sftp.listdir():
        sftp.chdir(f'{ROOT}/{dir}/results')
        print(sftp.getcwd())
        #print(sftp.listdir())
        #files_of_interest = [d for d in sftp.listdir() if d.split('.')[0].split('_')[2] == 'FP']
        files_of_interest = [d for d in sftp.listdir() if d.endswith('.json')]
        #filepaths_of_interest = [f'{sftp.getcwd()}/{d}' for d in files_of_interest]
        #print(filepaths_of_interest)
        #for file in filepaths_of_interest:
            #sftp.get(file, ROOT_LOCAL)
        for d in files_of_interest:
            local_path = ROOT_LOCAL + d
            remote_path = f'{sftp.getcwd()}/{d}'
            sftp.get(remote_path, local_path)


