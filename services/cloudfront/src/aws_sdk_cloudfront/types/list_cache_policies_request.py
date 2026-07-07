"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListCachePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cache_policy_type
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListCachePoliciesRequest(TypedDict, closed=True):
    type: NotRequired["aws_sdk_cloudfront.types.cache_policy_type.CachePolicyType"]
    """<p>A filter to return only the specified kinds of cache policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>"""
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of cache policies that you want in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListCachePoliciesRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListCachePoliciesRequest:
    out: ListCachePoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
