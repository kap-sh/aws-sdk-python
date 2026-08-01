"""Generated from Smithy shape ``com.amazonaws.route53#ErrorMessages``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.error_message

ErrorMessages: TypeAlias = list["capo_route_53.types.error_message.ErrorMessage"]


# --- restXml ser/de ---
def serialize_xml(value: ErrorMessages, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Message").text = str(item)


def deserialize_xml(el: Element) -> ErrorMessages:
    out: ErrorMessages = []
    for child in el.findall("Message"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: ErrorMessages, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> ErrorMessages:
    out: ErrorMessages = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
