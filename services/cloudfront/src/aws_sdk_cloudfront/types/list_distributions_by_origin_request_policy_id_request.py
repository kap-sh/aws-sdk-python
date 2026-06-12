"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByOriginRequestPolicyIdRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListDistributionsByOriginRequestPolicyIdRequest(TypedDict):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of distribution IDs that you want in the response.</p>"""
    origin_request_policy_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the origin request policy whose associated distribution IDs you want to list.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByOriginRequestPolicyIdRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListDistributionsByOriginRequestPolicyIdRequest:
    out: ListDistributionsByOriginRequestPolicyIdRequest = {}  # type: ignore[typeddict-item]
    return out
