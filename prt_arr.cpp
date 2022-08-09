void print_arr_check(uint32_t* arr, int begin, int end)
{
    for (int i = begin; i < end; i++){
        cout << *(arr+i) << " ";
    }
    cout << endl;
}