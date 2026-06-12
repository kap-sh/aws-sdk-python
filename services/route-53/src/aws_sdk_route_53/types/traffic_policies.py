"""Generated from Smithy shape ``com.amazonaws.route53#TrafficPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy

TrafficPolicies: TypeAlias = list["aws_sdk_route_53.types.traffic_policy.TrafficPolicy"]


# --- restXml ser/de ---
def serialize_xml(value: TrafficPolicies, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.traffic_policy

        aws_sdk_route_53.types.traffic_policy.serialize_xml(item, el, "TrafficPolicy")


def deserialize_xml(el: Element) -> TrafficPolicies:
    import aws_sdk_route_53.types.traffic_policy

    out: TrafficPolicies = []
    for child in el.findall("TrafficPolicy"):
        out.append(aws_sdk_route_53.types.traffic_policy.deserialize_xml(child))
    return out


def serialize_xml_flat(value: TrafficPolicies, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.traffic_policy

        aws_sdk_route_53.types.traffic_policy.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TrafficPolicies:
    import aws_sdk_route_53.types.traffic_policy

    out: TrafficPolicies = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.traffic_policy.deserialize_xml(child))
    return out
