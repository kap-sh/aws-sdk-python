"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetResponseHeadersPolicyConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetResponseHeadersPolicyConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetResponseHeadersPolicyConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetResponseHeadersPolicyConfigRequest:
    out: GetResponseHeadersPolicyConfigRequest = {}  # type: ignore[typeddict-item]
    return out
