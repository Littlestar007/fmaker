import subprocess
from cfmaker import compile_manager, ProjectConfig, inner_flag_opt

config = ProjectConfig(
	f_srcs=['test/src/**'],
	c_srcs=['test/src/**'],
	project_build_dir='test/build',
  f_exe_name='example.exe',
  c_lib_name='example.lib',
  static_libraries=['example.lib']
)

config.auto_add_intel_mpi()
config.auto_set_cc_options()
config.auto_set_fc_options()

#添加自定义选项
config.fc_options_debug += " -Dnofortls"
config.fc_options_release += " -Dnofortls"
# def gen_c_f90_inf(files):
#   '''生成c的f90接口文件'''
#   cmd = [
#     'python',
#     './generate_f90_interface.py',
#     " ".join([f"\"{dir}\"" for dir in files])
#   ]
#   subprocess.run(" ".join(cmd), shell=True)

cm = compile_manager(config)
#cm.add_function_after_c(gen_c_f90_inf)
cm.make()

