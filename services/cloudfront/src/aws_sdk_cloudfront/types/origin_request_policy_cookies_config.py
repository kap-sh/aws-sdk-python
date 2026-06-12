"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyCookiesConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cookie_names
    import aws_sdk_cloudfront.types.origin_request_policy_cookie_behavior


class OriginRequestPolicyCookiesConfig(TypedDict):
    cookie_behavior: "aws_sdk_cloudfront.types.origin_request_policy_cookie_behavior.OriginRequestPolicyCookieBehavior"
    """<p>Determines whether cookies in viewer requests are included in requests that CloudFront sends to the origin. Valid values are:</p> <ul> <li> <p> <code>none</code> – No cookies in viewer requests are included in requests that CloudFront sends to the origin. Even when this field is set to <code>none</code>, any cookies that are listed in a <code>CachePolicy</code> <i>are</i> included in origin requests.</p> </li> <li> <p> <code>whitelist</code> – Only the cookies in viewer requests that are listed in the <code>CookieNames</code> type are included in requests that CloudFront sends to the origin.</p> </li> <li> <p> <code>all</code> – All cookies in viewer requests are included in requests that CloudFront sends to the origin.</p> </li> <li> <p> <code>allExcept</code> – All cookies in viewer requests are included in requests that CloudFront sends to the origin, <i> <b>except</b> </i> for those listed in the <code>CookieNames</code> type, which are not included.</p> </li> </ul>"""
    cookies: NotRequired["aws_sdk_cloudfront.types.cookie_names.CookieNames"]


# --- restXml ser/de ---
def serialize_xml(
    value: OriginRequestPolicyCookiesConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.origin_request_policy_cookie_behavior

    aws_sdk_cloudfront.types.origin_request_policy_cookie_behavior.serialize_xml(
        value["cookie_behavior"], el, "CookieBehavior"
    )
    if "cookies" in value:
        import aws_sdk_cloudfront.types.cookie_names

        aws_sdk_cloudfront.types.cookie_names.serialize_xml(
            value["cookies"], el, "Cookies"
        )


def deserialize_xml(el: Element) -> OriginRequestPolicyCookiesConfig:
    out: OriginRequestPolicyCookiesConfig = {}  # type: ignore[typeddict-item]
    child_cookie_behavior = el.find("CookieBehavior")
    if child_cookie_behavior is not None:
        import aws_sdk_cloudfront.types.origin_request_policy_cookie_behavior

        out["cookie_behavior"] = (
            aws_sdk_cloudfront.types.origin_request_policy_cookie_behavior.deserialize_xml(
                child_cookie_behavior
            )
        )
    else:
        raise DeserializationError(
            "OriginRequestPolicyCookiesConfig.cookie_behavior required"
        )
    child_cookies = el.find("Cookies")
    if child_cookies is not None:
        import aws_sdk_cloudfront.types.cookie_names

        out["cookies"] = aws_sdk_cloudfront.types.cookie_names.deserialize_xml(
            child_cookies
        )
    return out
