"""Generated from Smithy shape ``com.amazonaws.route53#HealthChecks``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check

HealthChecks: TypeAlias = list["aws_sdk_route_53.types.health_check.HealthCheck"]


# --- restXml ser/de ---
def serialize_xml(value: HealthChecks, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.health_check

        aws_sdk_route_53.types.health_check.serialize_xml(item, el, "HealthCheck")


def deserialize_xml(el: Element) -> HealthChecks:
    import aws_sdk_route_53.types.health_check

    out: HealthChecks = []
    for child in el.findall("HealthCheck"):
        out.append(aws_sdk_route_53.types.health_check.deserialize_xml(child))
    return out


def serialize_xml_flat(value: HealthChecks, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.health_check

        aws_sdk_route_53.types.health_check.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> HealthChecks:
    import aws_sdk_route_53.types.health_check

    out: HealthChecks = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.health_check.deserialize_xml(child))
    return out
