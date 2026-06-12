"""Generated from Smithy shape ``com.amazonaws.route53#DelegationSetNameServers``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.dns_name

DelegationSetNameServers: TypeAlias = list["aws_sdk_route_53.types.dns_name.DNSName"]


# --- restXml ser/de ---
def serialize_xml(value: DelegationSetNameServers, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "NameServer").text = str(item)


def deserialize_xml(el: Element) -> DelegationSetNameServers:
    out: DelegationSetNameServers = []
    for child in el.findall("NameServer"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(
    value: DelegationSetNameServers, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> DelegationSetNameServers:
    out: DelegationSetNameServers = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
