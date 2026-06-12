"""Generated from Smithy shape ``com.amazonaws.route53#TrafficPolicyInstance``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.dns_name
    import aws_sdk_route_53.types.message
    import aws_sdk_route_53.types.resource_id
    import aws_sdk_route_53.types.rr_type
    import aws_sdk_route_53.types.traffic_policy_id
    import aws_sdk_route_53.types.traffic_policy_instance_id
    import aws_sdk_route_53.types.traffic_policy_instance_state
    import aws_sdk_route_53.types.traffic_policy_version
    import aws_sdk_route_53.types.ttl


class TrafficPolicyInstance(TypedDict):
    id: "aws_sdk_route_53.types.traffic_policy_instance_id.TrafficPolicyInstanceId"
    """<p>The ID that Amazon Route 53 assigned to the new traffic policy instance.</p>"""
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that Amazon Route 53 created resource record sets in.</p>"""
    name: "aws_sdk_route_53.types.dns_name.DNSName"
    """<p>The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance. </p>"""
    ttl: "aws_sdk_route_53.types.ttl.TTL"
    """<p>The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.</p>"""
    state: "aws_sdk_route_53.types.traffic_policy_instance_state.TrafficPolicyInstanceState"
    """<p>The value of <code>State</code> is one of the following values:</p> <dl> <dt>Applied</dt> <dd> <p>Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.</p> </dd> <dt>Creating</dt> <dd> <p>Route 53 is creating the resource record sets. Use <code>GetTrafficPolicyInstance</code> to confirm that the <code>CreateTrafficPolicyInstance</code> request completed successfully.</p> </dd> <dt>Failed</dt> <dd> <p>Route 53 wasn't able to create or update the resource record sets. When the value of <code>State</code> is <code>Failed</code>, see <code>Message</code> for an explanation of what caused the request to fail.</p> </dd> </dl>"""
    message: "aws_sdk_route_53.types.message.Message"
    """<p>If <code>State</code> is <code>Failed</code>, an explanation of the reason for the failure. If <code>State</code> is another value, <code>Message</code> is empty.</p>"""
    traffic_policy_id: "aws_sdk_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.</p>"""
    traffic_policy_version: (
        "aws_sdk_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    )
    """<p>The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.</p>"""
    traffic_policy_type: "aws_sdk_route_53.types.rr_type.RRType"
    """<p>The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrafficPolicyInstance, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "TTL").text = str(value["ttl"])
    SubElement(el, "State").text = str(value["state"])
    SubElement(el, "Message").text = str(value["message"])
    SubElement(el, "TrafficPolicyId").text = str(value["traffic_policy_id"])
    SubElement(el, "TrafficPolicyVersion").text = str(value["traffic_policy_version"])
    import aws_sdk_route_53.types.rr_type

    aws_sdk_route_53.types.rr_type.serialize_xml(
        value["traffic_policy_type"], el, "TrafficPolicyType"
    )


def deserialize_xml(el: Element) -> TrafficPolicyInstance:
    out: TrafficPolicyInstance = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("TrafficPolicyInstance.id required")
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        raise DeserializationError("TrafficPolicyInstance.hosted_zone_id required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("TrafficPolicyInstance.name required")
    child_ttl = el.find("TTL")
    if child_ttl is not None:
        out["ttl"] = int(child_ttl.text or "")
    else:
        raise DeserializationError("TrafficPolicyInstance.ttl required")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    else:
        raise DeserializationError("TrafficPolicyInstance.state required")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        raise DeserializationError("TrafficPolicyInstance.message required")
    child_traffic_policy_id = el.find("TrafficPolicyId")
    if child_traffic_policy_id is not None:
        out["traffic_policy_id"] = str(child_traffic_policy_id.text or "")
    else:
        raise DeserializationError("TrafficPolicyInstance.traffic_policy_id required")
    child_traffic_policy_version = el.find("TrafficPolicyVersion")
    if child_traffic_policy_version is not None:
        out["traffic_policy_version"] = int(child_traffic_policy_version.text or "")
    else:
        raise DeserializationError(
            "TrafficPolicyInstance.traffic_policy_version required"
        )
    child_traffic_policy_type = el.find("TrafficPolicyType")
    if child_traffic_policy_type is not None:
        import aws_sdk_route_53.types.rr_type

        out["traffic_policy_type"] = aws_sdk_route_53.types.rr_type.deserialize_xml(
            child_traffic_policy_type
        )
    else:
        raise DeserializationError("TrafficPolicyInstance.traffic_policy_type required")
    return out
