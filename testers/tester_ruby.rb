require "net/http"

url = ARGV.shift
uri = URI(url)
Net::HTTP.get(uri)
