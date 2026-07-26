"""Generated from Smithy shape ``com.amazonaws.s3control#AccessPointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_point

AccessPointList: TypeAlias = list["capo_s3_control.types.access_point.AccessPoint"]


# --- restXml ser/de ---
def serialize_xml(value: AccessPointList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.access_point

        capo_s3_control.types.access_point.serialize_xml(item, el, "AccessPoint")


def deserialize_xml(el: Element) -> AccessPointList:
    import capo_s3_control.types.access_point

    out: AccessPointList = []
    for child in el.findall("AccessPoint"):
        out.append(capo_s3_control.types.access_point.deserialize_xml(child))
    return out


def serialize_xml_flat(value: AccessPointList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.access_point

        capo_s3_control.types.access_point.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> AccessPointList:
    import capo_s3_control.types.access_point

    out: AccessPointList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.access_point.deserialize_xml(child))
    return out
