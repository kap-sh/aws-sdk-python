"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginRequestPolicyConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetOriginRequestPolicyConfigRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetOriginRequestPolicyConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetOriginRequestPolicyConfigRequest:
    out: GetOriginRequestPolicyConfigRequest = {}  # type: ignore[typeddict-item]
    return out
