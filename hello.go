package main

import "C"
import "fmt"

//export HelloWorld
func HelloWorld(name *C.char) {
    fmt.Printf("Hello, %s!\n", C.GoString(name))
}

func main() {}

