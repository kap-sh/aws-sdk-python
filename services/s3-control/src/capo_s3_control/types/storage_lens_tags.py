"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensTags``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.storage_lens_tag

StorageLensTags: TypeAlias = list[
    "capo_s3_control.types.storage_lens_tag.StorageLensTag"
]


# --- restXml ser/de ---
def serialize_xml(value: StorageLensTags, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.storage_lens_tag

        capo_s3_control.types.storage_lens_tag.serialize_xml(item, el, "Tag")


def deserialize_xml(el: Element) -> StorageLensTags:
    import capo_s3_control.types.storage_lens_tag

    out: StorageLensTags = []
    for child in el.findall("Tag"):
        out.append(capo_s3_control.types.storage_lens_tag.deserialize_xml(child))
    return out


def serialize_xml_flat(value: StorageLensTags, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.storage_lens_tag

        capo_s3_control.types.storage_lens_tag.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> StorageLensTags:
    import capo_s3_control.types.storage_lens_tag

    out: StorageLensTags = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.storage_lens_tag.deserialize_xml(child))
    return out
