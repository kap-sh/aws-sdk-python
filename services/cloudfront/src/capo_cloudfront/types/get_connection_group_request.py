"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetConnectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetConnectionGroupRequest(TypedDict, closed=True):
    identifier: "capo_cloudfront.types.string.string"
    """<p>The ID, name, or Amazon Resource Name (ARN) of the connection group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetConnectionGroupRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetConnectionGroupRequest:
    out: GetConnectionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
