
#ifndef SRC_COINMATE_PROXY_H_
#define SRC_COINMATE_PROXY_H_
#include <curlpp/Easy.hpp>
#include <chrono>

#include <imtjson/value.h>

class Proxy {
public:
  
  Proxy():

  std::string apiUrl;
  std::string privKey;
  std::string pubKey;
  cURLpp::Easy curl_handl;
  bool testnet = false;

  json::Value request(
	const std::string_view &verb,
	const std::string_view path,
	const json::Value &query = json::Value(),
	const json::Value &data = json::Value());

  bool hasKey() const;
  bool debug = false;

  static std::uint64_t now();

  void setTestnet(bool testnet);

  struct AuthData {
    std::string key;
    std::string signature;
    std::string expires;
  };

  AuthData signRequest(const std::string_view &verb,
		  const std::string_view &path,
		  const std::string_view &data);

  void urlEncode(const std::string_view &text, std::ostream &out);
  std::string buildPath(const std::string_view path, const json::Value &query);

};

#endif /* SRC_COINMATE_PROXY_H_ */


