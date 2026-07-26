"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListStreamingDistributionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ListStreamingDistributionsRequest(TypedDict, closed=True):
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The value that you provided for the <code>Marker</code> request parameter.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The value that you provided for the <code>MaxItems</code> request parameter.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStreamingDistributionsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListStreamingDistributionsRequest:
    out: ListStreamingDistributionsRequest = {}  # type: ignore[typeddict-item]
    return out
