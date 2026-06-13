# Changelog

## [0.4.0](https://github.com/kap-sh/aws-sdk-python/compare/aws-sdk-dynamodb-v0.3.0...aws-sdk-dynamodb-v0.4.0) (2026-06-13)


### Features

* add support for jmespath based operations ([a63b312](https://github.com/kap-sh/aws-sdk-python/commit/a63b312b58dabdc58a2917a684cd40e96b53d3ab))
* more predictable service module names ([2eea8d4](https://github.com/kap-sh/aws-sdk-python/commit/2eea8d436b791eec8a1c69ca0660495fbc877a01))


### Bug Fixes

* always read the response body before calling handle_response ([b45952b](https://github.com/kap-sh/aws-sdk-python/commit/b45952bedc3c1dfe0c15ac905aefeddb264b250e))
* close async responses with aclose instead of close ([51599f6](https://github.com/kap-sh/aws-sdk-python/commit/51599f6832a53fb85ea4d3fdca0169dd1c793b62))
* properly handle awsQuery based services' operations ([9c286e8](https://github.com/kap-sh/aws-sdk-python/commit/9c286e8cfa75177b85107ab11198f5dbf276e7b9))
* properly implement non-xml protocol based operations ([7ddcb16](https://github.com/kap-sh/aws-sdk-python/commit/7ddcb16980f6deefbff0d75a1a841974cd8b7e99))


### Miscellaneous

* add some useful ruff rules ([884120e](https://github.com/kap-sh/aws-sdk-python/commit/884120e36014edc03702f01c6860bb0fb7c9daae))
* bump zapros to 0.13.0 ([43f74e7](https://github.com/kap-sh/aws-sdk-python/commit/43f74e7b515b9d2db6120ba392278732f68224ac))


### Documentation

* fix pip install examples ([9c36b75](https://github.com/kap-sh/aws-sdk-python/commit/9c36b7551bf348fbb50d37b7e7bf447fa4a11480))


### Code Refactoring

* simplify auth logic ([975b158](https://github.com/kap-sh/aws-sdk-python/commit/975b158b69f2fd25310648b8183629d3eb8ca7bd))
