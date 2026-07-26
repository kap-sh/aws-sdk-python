"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetAnycastIpListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetAnycastIpListRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID of the Anycast static IP list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetAnycastIpListRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetAnycastIpListRequest:
    out: GetAnycastIpListRequest = {}  # type: ignore[typeddict-item]
    return out
