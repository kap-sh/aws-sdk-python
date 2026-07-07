"""Generated from Smithy shape ``com.amazonaws.lightsail#CacheSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.cookie_object
    import aws_sdk_lightsail.types.header_object
    import aws_sdk_lightsail.types.long
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.query_string_object


class CacheSettings(TypedDict, closed=True):
    default_ttl: NotRequired["aws_sdk_lightsail.types.long.long"]
    """<p>The default amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the content has been updated.</p> <note> <p>The value specified applies only when the origin does not add HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects.</p> </note>"""
    minimum_ttl: NotRequired["aws_sdk_lightsail.types.long.long"]
    """<p>The minimum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.</p> <p>A value of <code>0</code> must be specified for <code>minimumTTL</code> if the distribution is configured to forward all headers to the origin.</p>"""
    maximum_ttl: NotRequired["aws_sdk_lightsail.types.long.long"]
    """<p>The maximum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.</p> <p>The value specified applies only when the origin adds HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects.</p>"""
    allowed_http_methods: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The HTTP methods that are processed and forwarded to the distribution's origin.</p> <p>You can specify the following options:</p> <ul> <li> <p> <code>GET,HEAD</code> - The distribution forwards the <code>GET</code> and <code>HEAD</code> methods.</p> </li> <li> <p> <code>GET,HEAD,OPTIONS</code> - The distribution forwards the <code>GET</code>, <code>HEAD</code>, and <code>OPTIONS</code> methods.</p> </li> <li> <p> <code>GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE</code> - The distribution forwards the <code>GET</code>, <code>HEAD</code>, <code>OPTIONS</code>, <code>PUT</code>, <code>PATCH</code>, <code>POST</code>, and <code>DELETE</code> methods.</p> </li> </ul> <p>If you specify the third option, you might need to restrict access to your distribution's origin so users can't perform operations that you don't want them to. For example, you might not want users to have permission to delete objects from your origin.</p>"""
    cached_http_methods: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The HTTP method responses that are cached by your distribution.</p> <p>You can specify the following options:</p> <ul> <li> <p> <code>GET,HEAD</code> - The distribution caches responses to the <code>GET</code> and <code>HEAD</code> methods.</p> </li> <li> <p> <code>GET,HEAD,OPTIONS</code> - The distribution caches responses to the <code>GET</code>, <code>HEAD</code>, and <code>OPTIONS</code> methods.</p> </li> </ul>"""
    forwarded_cookies: NotRequired["aws_sdk_lightsail.types.cookie_object.CookieObject"]
    """<p>An object that describes the cookies that are forwarded to the origin. Your content is cached based on the cookies that are forwarded.</p>"""
    forwarded_headers: NotRequired["aws_sdk_lightsail.types.header_object.HeaderObject"]
    """<p>An object that describes the headers that are forwarded to the origin. Your content is cached based on the headers that are forwarded.</p>"""
    forwarded_query_strings: NotRequired[
        "aws_sdk_lightsail.types.query_string_object.QueryStringObject"
    ]
    """<p>An object that describes the query strings that are forwarded to the origin. Your content is cached based on the query strings that are forwarded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheSettings) -> dict:
    out: dict = {}
    if "default_ttl" in value:
        out["defaultTTL"] = value["default_ttl"]
    if "minimum_ttl" in value:
        out["minimumTTL"] = value["minimum_ttl"]
    if "maximum_ttl" in value:
        out["maximumTTL"] = value["maximum_ttl"]
    if "allowed_http_methods" in value:
        out["allowedHTTPMethods"] = value["allowed_http_methods"]
    if "cached_http_methods" in value:
        out["cachedHTTPMethods"] = value["cached_http_methods"]
    if "forwarded_cookies" in value:
        import aws_sdk_lightsail.types.cookie_object

        out["forwardedCookies"] = (
            aws_sdk_lightsail.types.cookie_object.serialize_aws_json_1_1(
                value["forwarded_cookies"]
            )
        )
    if "forwarded_headers" in value:
        import aws_sdk_lightsail.types.header_object

        out["forwardedHeaders"] = (
            aws_sdk_lightsail.types.header_object.serialize_aws_json_1_1(
                value["forwarded_headers"]
            )
        )
    if "forwarded_query_strings" in value:
        import aws_sdk_lightsail.types.query_string_object

        out["forwardedQueryStrings"] = (
            aws_sdk_lightsail.types.query_string_object.serialize_aws_json_1_1(
                value["forwarded_query_strings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheSettings:
    out: CacheSettings = {}  # type: ignore[typeddict-item]
    if "defaultTTL" in data:
        out["default_ttl"] = data["defaultTTL"]
    if "minimumTTL" in data:
        out["minimum_ttl"] = data["minimumTTL"]
    if "maximumTTL" in data:
        out["maximum_ttl"] = data["maximumTTL"]
    if "allowedHTTPMethods" in data:
        out["allowed_http_methods"] = data["allowedHTTPMethods"]
    if "cachedHTTPMethods" in data:
        out["cached_http_methods"] = data["cachedHTTPMethods"]
    if "forwardedCookies" in data:
        import aws_sdk_lightsail.types.cookie_object

        out["forwarded_cookies"] = (
            aws_sdk_lightsail.types.cookie_object.deserialize_aws_json_1_1(
                data["forwardedCookies"]
            )
        )
    if "forwardedHeaders" in data:
        import aws_sdk_lightsail.types.header_object

        out["forwarded_headers"] = (
            aws_sdk_lightsail.types.header_object.deserialize_aws_json_1_1(
                data["forwardedHeaders"]
            )
        )
    if "forwardedQueryStrings" in data:
        import aws_sdk_lightsail.types.query_string_object

        out["forwarded_query_strings"] = (
            aws_sdk_lightsail.types.query_string_object.deserialize_aws_json_1_1(
                data["forwardedQueryStrings"]
            )
        )
    return out
