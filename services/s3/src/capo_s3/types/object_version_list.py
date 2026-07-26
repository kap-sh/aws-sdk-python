"""Generated from Smithy shape ``com.amazonaws.s3#ObjectVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_version

ObjectVersionList: TypeAlias = list["capo_s3.types.object_version.ObjectVersion"]


# --- restXml ser/de ---
def serialize_xml(value: ObjectVersionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.object_version

        capo_s3.types.object_version.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ObjectVersionList:
    import capo_s3.types.object_version

    out: ObjectVersionList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.object_version.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ObjectVersionList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3.types.object_version

        capo_s3.types.object_version.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ObjectVersionList:
    import capo_s3.types.object_version

    out: ObjectVersionList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.object_version.deserialize_xml(child))
    return out
