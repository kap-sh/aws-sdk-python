"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginAccessControlConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetOriginAccessControlConfigRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The unique identifier of the origin access control.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetOriginAccessControlConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetOriginAccessControlConfigRequest:
    out: GetOriginAccessControlConfigRequest = {}  # type: ignore[typeddict-item]
    return out
