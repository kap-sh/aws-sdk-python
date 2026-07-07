"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListDistributionsByTrustStoreRequest(TypedDict, closed=True):
    trust_store_identifier: "aws_sdk_cloudfront.types.string.string"
    """<p>The distributions by trust store identifier.</p>"""
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of distributions that you want returned in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByTrustStoreRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListDistributionsByTrustStoreRequest:
    out: ListDistributionsByTrustStoreRequest = {}  # type: ignore[typeddict-item]
    return out
