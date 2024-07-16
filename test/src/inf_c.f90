module inf_c  
	implicit none  
	interface  
			subroutine c_print_hello(rank) bind(C, name="c_print_hello")
				integer,value:: rank
			end subroutine  
	end interface  
end module inf_c