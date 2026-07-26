"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.resource_id
    import capo_cloudfront.types.string


class DeleteTrustStoreRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.resource_id.ResourceId"
    """<p>The trust store's ID.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the trust store you are deleting.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteTrustStoreRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteTrustStoreRequest:
    out: DeleteTrustStoreRequest = {}  # type: ignore[typeddict-item]
    return out
