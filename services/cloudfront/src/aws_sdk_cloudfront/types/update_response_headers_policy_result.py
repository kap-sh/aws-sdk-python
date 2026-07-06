"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateResponseHeadersPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.response_headers_policy
    import aws_sdk_cloudfront.types.string


class UpdateResponseHeadersPolicyResult(TypedDict, closed=True):
    response_headers_policy: NotRequired[
        "aws_sdk_cloudfront.types.response_headers_policy.ResponseHeadersPolicy"
    ]
    """<p>A response headers policy.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the response headers policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateResponseHeadersPolicyResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "response_headers_policy" in value:
        import aws_sdk_cloudfront.types.response_headers_policy

        aws_sdk_cloudfront.types.response_headers_policy.serialize_xml(
            value["response_headers_policy"], el, "ResponseHeadersPolicy"
        )


def deserialize_xml(el: Element) -> UpdateResponseHeadersPolicyResult:
    out: UpdateResponseHeadersPolicyResult = {}  # type: ignore[typeddict-item]
    child_response_headers_policy = el.find("ResponseHeadersPolicy")
    if child_response_headers_policy is not None:
        import aws_sdk_cloudfront.types.response_headers_policy

        out["response_headers_policy"] = (
            aws_sdk_cloudfront.types.response_headers_policy.deserialize_xml(
                child_response_headers_policy
            )
        )
    return out
