"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListResponseHeadersPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.response_headers_policy_type
    import aws_sdk_cloudfront.types.string


class ListResponseHeadersPoliciesRequest(TypedDict):
    type: NotRequired[
        "aws_sdk_cloudfront.types.response_headers_policy_type.ResponseHeadersPolicyType"
    ]
    """<p>A filter to get only the specified kind of response headers policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Gets only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Gets only the custom policies created in your Amazon Web Services account.</p> </li> </ul>"""
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of response headers policies that you want to get in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListResponseHeadersPoliciesRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListResponseHeadersPoliciesRequest:
    out: ListResponseHeadersPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
