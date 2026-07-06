"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListRealtimeLogConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListRealtimeLogConfigsRequest(TypedDict, closed=True):
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of real-time log configurations that you want in the response.</p>"""
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListRealtimeLogConfigsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListRealtimeLogConfigsRequest:
    out: ListRealtimeLogConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
