#include <stdio.h>
#include <string.h>

int statistics(char *filename)
{
  FILE *data_file;
  char data_filename[50], c;
  int data_size, data_labels, data_features;
  strcpy(data_filename,"data/");
  strcat(data_filename,filename);
  data_file=fopen(data_filename, "r");
  fscanf(data_file,"%c %d \n", &c, &data_size);
  fscanf(data_file,"%c %d \n", &c, &data_features);
  fscanf(data_file,"%c %d \n", &c, &data_labels);

  int i = 0, j = 0;
  int total_labels = 0;
  int total_features_label = data_features + data_labels;
  float item = 0, lcard = 0, lden = 0;
  while(i < data_size) {
    j = 0;
    while(j < total_features_label) {
      fscanf(data_file,"%f \n",&item);
      if(j >= data_features) {
        total_labels = total_labels + item;
      }
      j++;
    }
    i++;
  }

  lcard = (float)total_labels/data_size;
  lden = (float)lcard/data_labels;

  printf("data_file: %s, número de labels: %d, lcard: %.6f, lden: %.6f \n",
   	  data_filename, total_labels, lcard, lden);
  printf("\n");
  fclose(data_file);
}
