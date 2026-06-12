"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyHeadersConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.headers
    import aws_sdk_cloudfront.types.origin_request_policy_header_behavior


class OriginRequestPolicyHeadersConfig(TypedDict):
    header_behavior: "aws_sdk_cloudfront.types.origin_request_policy_header_behavior.OriginRequestPolicyHeaderBehavior"
    """<p>Determines whether any HTTP headers are included in requests that CloudFront sends to the origin. Valid values are:</p> <ul> <li> <p> <code>none</code> – No HTTP headers in viewer requests are included in requests that CloudFront sends to the origin. Even when this field is set to <code>none</code>, any headers that are listed in a <code>CachePolicy</code> <i>are</i> included in origin requests.</p> </li> <li> <p> <code>whitelist</code> – Only the HTTP headers that are listed in the <code>Headers</code> type are included in requests that CloudFront sends to the origin.</p> </li> <li> <p> <code>allViewer</code> – All HTTP headers in viewer requests are included in requests that CloudFront sends to the origin.</p> </li> <li> <p> <code>allViewerAndWhitelistCloudFront</code> – All HTTP headers in viewer requests and the additional CloudFront headers that are listed in the <code>Headers</code> type are included in requests that CloudFront sends to the origin. The additional headers are added by CloudFront.</p> </li> <li> <p> <code>allExcept</code> – All HTTP headers in viewer requests are included in requests that CloudFront sends to the origin, <i> <b>except</b> </i> for those listed in the <code>Headers</code> type, which are not included.</p> </li> </ul>"""
    headers: NotRequired["aws_sdk_cloudfront.types.headers.Headers"]


# --- restXml ser/de ---
def serialize_xml(
    value: OriginRequestPolicyHeadersConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.origin_request_policy_header_behavior

    aws_sdk_cloudfront.types.origin_request_policy_header_behavior.serialize_xml(
        value["header_behavior"], el, "HeaderBehavior"
    )
    if "headers" in value:
        import aws_sdk_cloudfront.types.headers

        aws_sdk_cloudfront.types.headers.serialize_xml(value["headers"], el, "Headers")


def deserialize_xml(el: Element) -> OriginRequestPolicyHeadersConfig:
    out: OriginRequestPolicyHeadersConfig = {}  # type: ignore[typeddict-item]
    child_header_behavior = el.find("HeaderBehavior")
    if child_header_behavior is not None:
        import aws_sdk_cloudfront.types.origin_request_policy_header_behavior

        out["header_behavior"] = (
            aws_sdk_cloudfront.types.origin_request_policy_header_behavior.deserialize_xml(
                child_header_behavior
            )
        )
    else:
        raise DeserializationError(
            "OriginRequestPolicyHeadersConfig.header_behavior required"
        )
    child_headers = el.find("Headers")
    if child_headers is not None:
        import aws_sdk_cloudfront.types.headers

        out["headers"] = aws_sdk_cloudfront.types.headers.deserialize_xml(child_headers)
    return out
