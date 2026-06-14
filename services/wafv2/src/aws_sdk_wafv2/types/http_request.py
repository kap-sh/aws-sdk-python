"""Generated from Smithy shape ``com.amazonaws.wafv2#HTTPRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.country
    import aws_sdk_wafv2.types.http_headers
    import aws_sdk_wafv2.types.http_method
    import aws_sdk_wafv2.types.http_version
    import aws_sdk_wafv2.types.ip_string
    import aws_sdk_wafv2.types.uri_string


class HTTPRequest(TypedDict):
    client_ip: NotRequired["aws_sdk_wafv2.types.ip_string.IPString"]
    """<p>The IP address that the request originated from. If the web ACL is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:</p> <ul> <li> <p> <code>c-ip</code>, if the viewer did not use an HTTP proxy or a load balancer to send the request</p> </li> <li> <p> <code>x-forwarded-for</code>, if the viewer did use an HTTP proxy or a load balancer to send the request</p> </li> </ul>"""
    country: NotRequired["aws_sdk_wafv2.types.country.Country"]
    r"""<p>The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a>.</p>"""
    uri: NotRequired["aws_sdk_wafv2.types.uri_string.URIString"]
    """<p>The URI path of the request, which identifies the resource, for example, <code>/images/daily-ad.jpg</code>.</p>"""
    method: NotRequired["aws_sdk_wafv2.types.http_method.HTTPMethod"]
    """<p>The HTTP method specified in the sampled web request. </p>"""
    http_version: NotRequired["aws_sdk_wafv2.types.http_version.HTTPVersion"]
    """<p>The HTTP version specified in the sampled web request, for example, <code>HTTP/1.1</code>.</p>"""
    headers: NotRequired["aws_sdk_wafv2.types.http_headers.HTTPHeaders"]
    """<p>A complex type that contains the name and value for each header in the sampled web request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HTTPRequest) -> dict:
    out: dict = {}
    if "client_ip" in value:
        out["ClientIP"] = value["client_ip"]
    if "country" in value:
        out["Country"] = value["country"]
    if "uri" in value:
        out["URI"] = value["uri"]
    if "method" in value:
        out["Method"] = value["method"]
    if "http_version" in value:
        out["HTTPVersion"] = value["http_version"]
    if "headers" in value:
        import aws_sdk_wafv2.types.http_headers

        out["Headers"] = aws_sdk_wafv2.types.http_headers.serialize_aws_json_1_1(
            value["headers"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HTTPRequest:
    out: HTTPRequest = {}  # type: ignore[typeddict-item]
    if "ClientIP" in data:
        out["client_ip"] = data["ClientIP"]
    if "Country" in data:
        out["country"] = data["Country"]
    if "URI" in data:
        out["uri"] = data["URI"]
    if "Method" in data:
        out["method"] = data["Method"]
    if "HTTPVersion" in data:
        out["http_version"] = data["HTTPVersion"]
    if "Headers" in data:
        import aws_sdk_wafv2.types.http_headers

        out["headers"] = aws_sdk_wafv2.types.http_headers.deserialize_aws_json_1_1(
            data["Headers"]
        )
    return out
