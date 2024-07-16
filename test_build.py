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

compile_manager(config).make()

