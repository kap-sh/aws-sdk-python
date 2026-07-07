"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListInvalidationsForDistributionTenantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListInvalidationsForDistributionTenantRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution tenant.</p>"""
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of invalidations to return for the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListInvalidationsForDistributionTenantRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListInvalidationsForDistributionTenantRequest:
    out: ListInvalidationsForDistributionTenantRequest = {}  # type: ignore[typeddict-item]
    return out
