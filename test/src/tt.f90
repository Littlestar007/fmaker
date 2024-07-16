module module2  
	implicit none  

	contains


	subroutine sum(a, b, c)
		integer:: a, b, c
	
		c = a + b
		
	end subroutine sum
end module module2