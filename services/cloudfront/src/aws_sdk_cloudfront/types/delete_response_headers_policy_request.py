"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteResponseHeadersPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteResponseHeadersPolicyRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier for the response headers policy that you are deleting.</p> <p>To get the identifier, you can use <code>ListResponseHeadersPolicies</code>.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version of the response headers policy that you are deleting.</p> <p>The version is the response headers policy's <code>ETag</code> value, which you can get using <code>ListResponseHeadersPolicies</code>, <code>GetResponseHeadersPolicy</code>, or <code>GetResponseHeadersPolicyConfig</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteResponseHeadersPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteResponseHeadersPolicyRequest:
    out: DeleteResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
