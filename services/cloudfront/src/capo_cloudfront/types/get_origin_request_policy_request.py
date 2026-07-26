"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginRequestPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetOriginRequestPolicyRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetOriginRequestPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetOriginRequestPolicyRequest:
    out: GetOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
