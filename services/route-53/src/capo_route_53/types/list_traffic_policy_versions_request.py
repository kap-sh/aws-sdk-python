"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPolicyVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_version_marker


class ListTrafficPolicyVersionsRequest(TypedDict, closed=True):
    id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>Specify the value of <code>Id</code> of the traffic policy for which you want to list all versions.</p>"""
    traffic_policy_version_marker: NotRequired[
        "capo_route_53.types.traffic_policy_version_marker.TrafficPolicyVersionMarker"
    ]
    """<p>For your first request to <code>ListTrafficPolicyVersions</code>, don't include the <code>TrafficPolicyVersionMarker</code> parameter.</p> <p>If you have more traffic policy versions than the value of <code>MaxItems</code>, <code>ListTrafficPolicyVersions</code> returns only the first group of <code>MaxItems</code> versions. To get more traffic policy versions, submit another <code>ListTrafficPolicyVersions</code> request. For the value of <code>TrafficPolicyVersionMarker</code>, specify the value of <code>TrafficPolicyVersionMarker</code> in the previous response.</p>"""
    max_items: NotRequired["int"]
    """<p>The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than <code>MaxItems</code> versions, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of the <code>TrafficPolicyVersionMarker</code> element is the ID of the first version that Route 53 will return if you submit another request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTrafficPolicyVersionsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListTrafficPolicyVersionsRequest:
    out: ListTrafficPolicyVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
