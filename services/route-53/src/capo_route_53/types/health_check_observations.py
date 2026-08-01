"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckObservations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.health_check_observation

HealthCheckObservations: TypeAlias = list[
    "capo_route_53.types.health_check_observation.HealthCheckObservation"
]


# --- restXml ser/de ---
def serialize_xml(value: HealthCheckObservations, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.health_check_observation

        capo_route_53.types.health_check_observation.serialize_xml(
            item, el, "HealthCheckObservation"
        )


def deserialize_xml(el: Element) -> HealthCheckObservations:
    import capo_route_53.types.health_check_observation

    out: HealthCheckObservations = []
    for child in el.findall("HealthCheckObservation"):
        out.append(capo_route_53.types.health_check_observation.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: HealthCheckObservations, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.health_check_observation

        capo_route_53.types.health_check_observation.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> HealthCheckObservations:
    import capo_route_53.types.health_check_observation

    out: HealthCheckObservations = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.health_check_observation.deserialize_xml(child))
    return out
