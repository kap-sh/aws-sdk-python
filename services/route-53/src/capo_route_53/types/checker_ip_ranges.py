"""Generated from Smithy shape ``com.amazonaws.route53#CheckerIpRanges``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.ip_address_cidr

CheckerIpRanges: TypeAlias = list["capo_route_53.types.ip_address_cidr.IPAddressCidr"]


# --- restXml ser/de ---
def serialize_xml(value: CheckerIpRanges, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "member").text = str(item)


def deserialize_xml(el: Element) -> CheckerIpRanges:
    out: CheckerIpRanges = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: CheckerIpRanges, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> CheckerIpRanges:
    out: CheckerIpRanges = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
