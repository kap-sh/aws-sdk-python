"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByResponseHeadersPolicyIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ListDistributionsByResponseHeadersPolicyIdRequest(TypedDict, closed=True):
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The maximum number of distribution IDs that you want to get in the response.</p>"""
    response_headers_policy_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the response headers policy whose associated distribution IDs you want to list.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByResponseHeadersPolicyIdRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListDistributionsByResponseHeadersPolicyIdRequest:
    out: ListDistributionsByResponseHeadersPolicyIdRequest = {}  # type: ignore[typeddict-item]
    return out
