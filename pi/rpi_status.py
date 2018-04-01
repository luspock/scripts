import subprocess

def execute_command(cmd):
	print('start executing cmd...')
	s = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	stdoutinfo, stderrinfo = s.communicate()
	print('errinfo is {}'.format(stderrinfo))
	print('outinfo is {}'.format(stdoutinfo))
	print('finish executing cmd...')
	return s.returncode

if __name__ == '__main__':
	cmd = '/opt/vc/bin/vcgencmd measure_temp'
	result = execute_command(cmd)
	print(result)
