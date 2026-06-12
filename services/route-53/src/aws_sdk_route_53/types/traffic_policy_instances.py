"""Generated from Smithy shape ``com.amazonaws.route53#TrafficPolicyInstances``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy_instance

TrafficPolicyInstances: TypeAlias = list[
    "aws_sdk_route_53.types.traffic_policy_instance.TrafficPolicyInstance"
]


# --- restXml ser/de ---
def serialize_xml(value: TrafficPolicyInstances, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.traffic_policy_instance

        aws_sdk_route_53.types.traffic_policy_instance.serialize_xml(
            item, el, "TrafficPolicyInstance"
        )


def deserialize_xml(el: Element) -> TrafficPolicyInstances:
    import aws_sdk_route_53.types.traffic_policy_instance

    out: TrafficPolicyInstances = []
    for child in el.findall("TrafficPolicyInstance"):
        out.append(
            aws_sdk_route_53.types.traffic_policy_instance.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: TrafficPolicyInstances, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.traffic_policy_instance

        aws_sdk_route_53.types.traffic_policy_instance.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TrafficPolicyInstances:
    import aws_sdk_route_53.types.traffic_policy_instance

    out: TrafficPolicyInstances = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_route_53.types.traffic_policy_instance.deserialize_xml(child)
        )
    return out
