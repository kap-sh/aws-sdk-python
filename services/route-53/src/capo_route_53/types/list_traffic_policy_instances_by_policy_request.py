"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPolicyInstancesByPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.resource_id
    import capo_route_53.types.rr_type
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_version


class ListTrafficPolicyInstancesByPolicyRequest(TypedDict, closed=True):
    traffic_policy_id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID of the traffic policy for which you want to list traffic policy instances.</p>"""
    traffic_policy_version: (
        "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    )
    """<p>The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by <code>TrafficPolicyId</code>.</p>"""
    hosted_zone_id_marker: NotRequired["capo_route_53.types.resource_id.ResourceId"]
    """<p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request. </p> <p>For the value of <code>hostedzoneid</code>, specify the value of <code>HostedZoneIdMarker</code> from the previous response, which is the hosted zone ID of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>"""
    traffic_policy_instance_name_marker: NotRequired[
        "capo_route_53.types.dns_name.DNSName"
    ]
    """<p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request.</p> <p>For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>"""
    traffic_policy_instance_type_marker: NotRequired[
        "capo_route_53.types.rr_type.RRType"
    ]
    """<p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request.</p> <p>For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>"""
    max_items: NotRequired["int"]
    """<p>The maximum number of traffic policy instances to be included in the response body for this request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTrafficPolicyInstancesByPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListTrafficPolicyInstancesByPolicyRequest:
    out: ListTrafficPolicyInstancesByPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
