arr = [9,5,4,2,1,6,7,10]
console.log(arr)
for(i = 1; i < arr.length; i++){
    j = i-1
    key = arr[i]
    while (j >= 0 && arr[j] > key){
        arr[j+1] = arr[j]
        j--;
    }
    
    arr[j+1] = key

}
console.log(arr)