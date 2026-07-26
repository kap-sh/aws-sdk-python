"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListVpcOriginsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ListVpcOriginsRequest(TypedDict, closed=True):
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The marker associated with the VPC origins list.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The maximum number of items included in the list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListVpcOriginsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListVpcOriginsRequest:
    out: ListVpcOriginsRequest = {}  # type: ignore[typeddict-item]
    return out
