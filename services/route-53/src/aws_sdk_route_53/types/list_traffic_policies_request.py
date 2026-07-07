"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy_id


class ListTrafficPoliciesRequest(TypedDict, closed=True):
    traffic_policy_id_marker: NotRequired[
        "aws_sdk_route_53.types.traffic_policy_id.TrafficPolicyId"
    ]
    """<p>(Conditional) For your first request to <code>ListTrafficPolicies</code>, don't include the <code>TrafficPolicyIdMarker</code> parameter.</p> <p>If you have more traffic policies than the value of <code>MaxItems</code>, <code>ListTrafficPolicies</code> returns only the first <code>MaxItems</code> traffic policies. To get the next group of policies, submit another request to <code>ListTrafficPolicies</code>. For the value of <code>TrafficPolicyIdMarker</code>, specify the value of <code>TrafficPolicyIdMarker</code> that was returned in the previous response.</p>"""
    max_items: NotRequired["int"]
    """<p>(Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than <code>MaxItems</code> traffic policies, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of <code>TrafficPolicyIdMarker</code> is the ID of the first traffic policy that Route 53 will return if you submit another request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTrafficPoliciesRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListTrafficPoliciesRequest:
    out: ListTrafficPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
