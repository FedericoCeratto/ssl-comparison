# nim c -d:ssl -p:. tester_nim.nim

import httpclient
from os import paramStr
let a = $getContent(paramStr(1))
