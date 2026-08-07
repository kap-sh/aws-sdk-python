"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.list_storage_lens_configuration_entry

StorageLensConfigurationList: TypeAlias = list[
    "capo_s3_control.types.list_storage_lens_configuration_entry.ListStorageLensConfigurationEntry"
]


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensConfigurationList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.list_storage_lens_configuration_entry

        capo_s3_control.types.list_storage_lens_configuration_entry.serialize_xml(
            item, el, "StorageLensConfiguration"
        )


def deserialize_xml(el: Element) -> StorageLensConfigurationList:
    import capo_s3_control.types.list_storage_lens_configuration_entry

    out: StorageLensConfigurationList = []
    for child in el.findall("StorageLensConfiguration"):
        out.append(
            capo_s3_control.types.list_storage_lens_configuration_entry.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: StorageLensConfigurationList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.list_storage_lens_configuration_entry

        capo_s3_control.types.list_storage_lens_configuration_entry.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> StorageLensConfigurationList:
    import capo_s3_control.types.list_storage_lens_configuration_entry

    out: StorageLensConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.list_storage_lens_configuration_entry.deserialize_xml(
                child
            )
        )
    return out
