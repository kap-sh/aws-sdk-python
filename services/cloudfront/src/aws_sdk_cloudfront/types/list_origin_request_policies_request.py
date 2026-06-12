"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListOriginRequestPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.origin_request_policy_type
    import aws_sdk_cloudfront.types.string


class ListOriginRequestPoliciesRequest(TypedDict):
    type: NotRequired[
        "aws_sdk_cloudfront.types.origin_request_policy_type.OriginRequestPolicyType"
    ]
    """<p>A filter to return only the specified kinds of origin request policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>"""
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of origin request policies that you want in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListOriginRequestPoliciesRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListOriginRequestPoliciesRequest:
    out: ListOriginRequestPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
