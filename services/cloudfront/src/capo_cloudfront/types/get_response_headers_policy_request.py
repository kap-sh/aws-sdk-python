"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetResponseHeadersPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetResponseHeadersPolicyRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetResponseHeadersPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetResponseHeadersPolicyRequest:
    out: GetResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
