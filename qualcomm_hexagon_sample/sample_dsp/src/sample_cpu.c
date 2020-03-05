#include "sample_cpu.h"
#include "sample_dsp.h"
#include "rpcmem.h"
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char* argv[])
{

		float num3,num4;
		num3 = 16777215.0;
		num4 = 2.3;

		int8_t *num1;
		int8_t num2;		

		rpcmem_init();

		if (0 == (num1 = (int8_t*)rpcmem_alloc(0, RPCMEM_HEAP_DEFAULT, sizeof(int8_t)))) {
				printf("Error: alloc failed\n");
		}

		*num1 = 7;
		num2 = 5;
	
					

		printf("Before DSP RPC Call num1 = %d num2 = %d\n", *num1 , num2);

		if (0 != sample_dsp_sum_int(num1,&num2)) {
				printf("Error: compute on DSP failed\n");
		}

		printf("After DSP RPC Call num1 = %d num2 = %d\n", *num1 , num2);
		if(argc == 2) {
		
		printf("Before DSP RPC Call num3 = %f num4 = %f\n", num3 , num4);
		sample_dsp_sum_float(&num3,&num4);
		printf("After DSP RPC Call num3 = %f num4 = %f\n", num3 , num4);
		sample_dsp_sum_float(&num3,&num4);
		printf("After DSP RPC Call num3 = %f num4 = %f\n", num3 , num4);
		}

		if (num1) {
				rpcmem_free(num1);
		}
		rpcmem_deinit();
		
		return 0;
}
