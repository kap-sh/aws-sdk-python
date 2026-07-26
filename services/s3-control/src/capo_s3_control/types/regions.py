"""Generated from Smithy shape ``com.amazonaws.s3control#Regions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_aws_region

Regions: TypeAlias = list["capo_s3_control.types.s3_aws_region.S3AWSRegion"]


# --- restXml ser/de ---
def serialize_xml(value: Regions, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Region").text = str(item)


def deserialize_xml(el: Element) -> Regions:
    out: Regions = []
    for child in el.findall("Region"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: Regions, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> Regions:
    out: Regions = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
