"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPolicyInstancesByHostedZoneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.dns_name
    import aws_sdk_route_53.types.resource_id
    import aws_sdk_route_53.types.rr_type


class ListTrafficPolicyInstancesByHostedZoneRequest(TypedDict, closed=True):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that you want to list traffic policy instances for.</p>"""
    traffic_policy_instance_name_marker: NotRequired[
        "aws_sdk_route_53.types.dns_name.DNSName"
    ]
    """<p>If the value of <code>IsTruncated</code> in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>"""
    traffic_policy_instance_type_marker: NotRequired[
        "aws_sdk_route_53.types.rr_type.RRType"
    ]
    """<p>If the value of <code>IsTruncated</code> in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>"""
    max_items: NotRequired["int"]
    """<p>The maximum number of traffic policy instances to be included in the response body for this request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTrafficPolicyInstancesByHostedZoneRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListTrafficPolicyInstancesByHostedZoneRequest:
    out: ListTrafficPolicyInstancesByHostedZoneRequest = {}  # type: ignore[typeddict-item]
    return out
