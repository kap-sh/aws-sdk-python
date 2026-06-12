"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListStreamingDistributionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListStreamingDistributionsRequest(TypedDict):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value that you provided for the <code>Marker</code> request parameter.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The value that you provided for the <code>MaxItems</code> request parameter.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStreamingDistributionsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListStreamingDistributionsRequest:
    out: ListStreamingDistributionsRequest = {}  # type: ignore[typeddict-item]
    return out
