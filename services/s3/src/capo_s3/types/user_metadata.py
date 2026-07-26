"""Generated from Smithy shape ``com.amazonaws.s3#UserMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.metadata_entry

UserMetadata: TypeAlias = list["capo_s3.types.metadata_entry.MetadataEntry"]


# --- restXml ser/de ---
def serialize_xml(value: UserMetadata, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.metadata_entry

        capo_s3.types.metadata_entry.serialize_xml(item, el, "MetadataEntry")


def deserialize_xml(el: Element) -> UserMetadata:
    import capo_s3.types.metadata_entry

    out: UserMetadata = []
    for child in el.findall("MetadataEntry"):
        out.append(capo_s3.types.metadata_entry.deserialize_xml(child))
    return out


def serialize_xml_flat(value: UserMetadata, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3.types.metadata_entry

        capo_s3.types.metadata_entry.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> UserMetadata:
    import capo_s3.types.metadata_entry

    out: UserMetadata = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.metadata_entry.deserialize_xml(child))
    return out
