program main  
	use mpi  
	use inf_c  
	use module2

	implicit none  
	integer :: ierr, rank  

	! 初始化MPI  
	call MPI_Init(ierr)  
	call MPI_Comm_rank(MPI_COMM_WORLD, rank, ierr)  

	! 打印进程号  
	print *, 'Hello from Fortran process', rank  

	! 调用C函数  
	call c_print_hello(rank)  
	call sum(1, 2, ierr)

	! 结束MPI  
	call MPI_Finalize(ierr)  
end program main