"""Generated from Smithy shape ``com.amazonaws.route53#ListReusableDelegationSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.page_marker


class ListReusableDelegationSetsRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_route_53.types.page_marker.PageMarker"]
    """<p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more reusable delegation sets. To get another group, submit another <code>ListReusableDelegationSets</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more reusable delegation sets to get.</p>"""
    max_items: NotRequired["int"]
    """<p>The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListReusableDelegationSetsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListReusableDelegationSetsRequest:
    out: ListReusableDelegationSetsRequest = {}  # type: ignore[typeddict-item]
    return out
