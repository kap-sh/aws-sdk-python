"""Generated from Smithy shape ``com.amazonaws.s3control#RegionCreationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.region

RegionCreationList: TypeAlias = list["capo_s3_control.types.region.Region"]


# --- restXml ser/de ---
def serialize_xml(value: RegionCreationList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.region

        capo_s3_control.types.region.serialize_xml(item, el, "Region")


def deserialize_xml(el: Element) -> RegionCreationList:
    import capo_s3_control.types.region

    out: RegionCreationList = []
    for child in el.findall("Region"):
        out.append(capo_s3_control.types.region.deserialize_xml(child))
    return out


def serialize_xml_flat(value: RegionCreationList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.region

        capo_s3_control.types.region.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> RegionCreationList:
    import capo_s3_control.types.region

    out: RegionCreationList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.region.deserialize_xml(child))
    return out
