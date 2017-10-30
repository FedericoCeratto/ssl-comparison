
// cd testers && /usr/lib/go-1.9/bin/go build tester_go.go

package main

import (
	"net/http"
	"os"
)

func main() {
	_, err := http.Get(os.Args[1])
	if err == nil {
		os.Exit(0)
	}
	os.Exit(1)
}

