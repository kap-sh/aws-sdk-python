"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetTrustStoreRequest(TypedDict, closed=True):
    identifier: "capo_cloudfront.types.string.string"
    """<p>The trust store's identifier.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetTrustStoreRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetTrustStoreRequest:
    out: GetTrustStoreRequest = {}  # type: ignore[typeddict-item]
    return out
