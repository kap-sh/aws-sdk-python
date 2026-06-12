"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetCachePolicyConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetCachePolicyConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetCachePolicyConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetCachePolicyConfigRequest:
    out: GetCachePolicyConfigRequest = {}  # type: ignore[typeddict-item]
    return out
