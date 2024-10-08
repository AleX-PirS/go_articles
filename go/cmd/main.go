package main

import (
	"fmt"
	"log"
	"os"

	"github.com/unidoc/unipdf/v3/model"
)

var files = []string{"../articles/Kick_back_CMP.pdf"} //, "../articles/100MS_SAR_ADC.pdf", "../articles/Low_power_SAR_ADC.pdf"}

func main() {
	f, err := os.Open(files[0])
	if err != nil {
		log.Fatalf("Failed to open PDF: %v\n", err)
	}
	defer f.Close()

	pdfReader, err := model.NewPdfReader(f)
	if err != nil {
		log.Fatalf("Failed to read PDF: %v\n", err)
	}

	page, err := pdfReader.GetPage(1)
	if err != nil {
		log.Fatalf("Failed to retrieve page %d: %v\n", 1, err)
	}
	a, _ := page.GetContentStreams()
	fmt.Println(a[3])
	// ex, _ := extractor.New(page)
	// text,_ := ex.ExtractText()
	// fmt.Println(text)
}
