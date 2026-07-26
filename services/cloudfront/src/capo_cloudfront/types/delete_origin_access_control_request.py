"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteOriginAccessControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DeleteOriginAccessControlRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The unique identifier of the origin access control that you are deleting.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version (<code>ETag</code> value) of the origin access control that you are deleting.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteOriginAccessControlRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteOriginAccessControlRequest:
    out: DeleteOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
    return out
