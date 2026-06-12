"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteOriginRequestPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteOriginRequestPolicyRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use <code>ListOriginRequestPolicies</code>.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version of the origin request policy that you are deleting. The version is the origin request policy's <code>ETag</code> value, which you can get using <code>ListOriginRequestPolicies</code>, <code>GetOriginRequestPolicy</code>, or <code>GetOriginRequestPolicyConfig</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteOriginRequestPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteOriginRequestPolicyRequest:
    out: DeleteOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
