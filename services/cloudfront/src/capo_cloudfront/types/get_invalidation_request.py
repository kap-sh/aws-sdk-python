"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetInvalidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetInvalidationRequest(TypedDict, closed=True):
    distribution_id: "capo_cloudfront.types.string.string"
    """<p>The distribution's ID.</p>"""
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetInvalidationRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetInvalidationRequest:
    out: GetInvalidationRequest = {}  # type: ignore[typeddict-item]
    return out
