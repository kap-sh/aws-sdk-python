"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.list_storage_lens_group_entry

StorageLensGroupList: TypeAlias = list[
    "capo_s3_control.types.list_storage_lens_group_entry.ListStorageLensGroupEntry"
]


# --- restXml ser/de ---
def serialize_xml(value: StorageLensGroupList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.list_storage_lens_group_entry

        capo_s3_control.types.list_storage_lens_group_entry.serialize_xml(
            item, el, "StorageLensGroup"
        )


def deserialize_xml(el: Element) -> StorageLensGroupList:
    import capo_s3_control.types.list_storage_lens_group_entry

    out: StorageLensGroupList = []
    for child in el.findall("StorageLensGroup"):
        out.append(
            capo_s3_control.types.list_storage_lens_group_entry.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(value: StorageLensGroupList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.list_storage_lens_group_entry

        capo_s3_control.types.list_storage_lens_group_entry.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> StorageLensGroupList:
    import capo_s3_control.types.list_storage_lens_group_entry

    out: StorageLensGroupList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.list_storage_lens_group_entry.deserialize_xml(child)
        )
    return out
