"""Generated from Smithy shape ``com.amazonaws.route53#TrafficPolicySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.traffic_policy_summary

TrafficPolicySummaries: TypeAlias = list[
    "capo_route_53.types.traffic_policy_summary.TrafficPolicySummary"
]


# --- restXml ser/de ---
def serialize_xml(value: TrafficPolicySummaries, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.traffic_policy_summary

        capo_route_53.types.traffic_policy_summary.serialize_xml(
            item, el, "TrafficPolicySummary"
        )


def deserialize_xml(el: Element) -> TrafficPolicySummaries:
    import capo_route_53.types.traffic_policy_summary

    out: TrafficPolicySummaries = []
    for child in el.findall("TrafficPolicySummary"):
        out.append(capo_route_53.types.traffic_policy_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: TrafficPolicySummaries, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.traffic_policy_summary

        capo_route_53.types.traffic_policy_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TrafficPolicySummaries:
    import capo_route_53.types.traffic_policy_summary

    out: TrafficPolicySummaries = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.traffic_policy_summary.deserialize_xml(child))
    return out
