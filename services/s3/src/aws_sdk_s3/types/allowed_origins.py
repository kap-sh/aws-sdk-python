"""Generated from Smithy shape ``com.amazonaws.s3#AllowedOrigins``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.allowed_origin

AllowedOrigins: TypeAlias = list["aws_sdk_s3.types.allowed_origin.AllowedOrigin"]


# --- restXml ser/de ---
def serialize_xml(value: AllowedOrigins, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "member").text = str(item)


def deserialize_xml(el: Element) -> AllowedOrigins:
    out: AllowedOrigins = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: AllowedOrigins, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> AllowedOrigins:
    out: AllowedOrigins = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
