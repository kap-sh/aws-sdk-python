"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetVpcOriginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetVpcOriginRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The VPC origin ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetVpcOriginRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetVpcOriginRequest:
    out: GetVpcOriginRequest = {}  # type: ignore[typeddict-item]
    return out
