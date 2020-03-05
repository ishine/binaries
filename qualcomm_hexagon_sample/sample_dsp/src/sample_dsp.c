/*==============================================================================
  Copyright (c) 2012-2014 Qualcomm Technologies, Inc.
  All rights reserved. Qualcomm Proprietary and Confidential.
==============================================================================*/

#include <stdio.h>
#include "HAP_farf.h"
#include "sample_dsp.h"

int8_t sample_dsp_sum_int(int8_t * a, int8_t* b)
{
  
  *a = *a + 1;
  *b = *b + 1;	
  FARF(ALWAYS, "===============     DSP: sum result %d  %d===============", *a ,*b);
  return 0;
}

int8_t sample_dsp_sum_float(float * a, float* b)
{

  *a = *a + 1.0;
  *b = *b + 1.1;
  FARF(ALWAYS, "===============     DSP: sum result %f  %f===============", *a ,*b);
  return 0;
}

