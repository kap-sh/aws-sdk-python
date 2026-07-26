"""Generated from Smithy shape ``com.amazonaws.route53#ListHealthChecksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.page_marker


class ListHealthChecksRequest(TypedDict, closed=True):
    marker: NotRequired["capo_route_53.types.page_marker.PageMarker"]
    """<p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more health checks. To get another group, submit another <code>ListHealthChecks</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more health checks to get.</p>"""
    max_items: NotRequired["int"]
    """<p>The maximum number of health checks that you want <code>ListHealthChecks</code> to return in response to the current request. Amazon Route 53 returns a maximum of 1000 items. If you set <code>MaxItems</code> to a value greater than 1000, Route 53 returns only the first 1000 health checks. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListHealthChecksRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListHealthChecksRequest:
    out: ListHealthChecksRequest = {}  # type: ignore[typeddict-item]
    return out
