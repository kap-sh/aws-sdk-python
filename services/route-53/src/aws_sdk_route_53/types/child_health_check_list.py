"""Generated from Smithy shape ``com.amazonaws.route53#ChildHealthCheckList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check_id

ChildHealthCheckList: TypeAlias = list[
    "aws_sdk_route_53.types.health_check_id.HealthCheckId"
]


# --- restXml ser/de ---
def serialize_xml(value: ChildHealthCheckList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "ChildHealthCheck").text = str(item)


def deserialize_xml(el: Element) -> ChildHealthCheckList:
    out: ChildHealthCheckList = []
    for child in el.findall("ChildHealthCheck"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: ChildHealthCheckList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> ChildHealthCheckList:
    out: ChildHealthCheckList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
