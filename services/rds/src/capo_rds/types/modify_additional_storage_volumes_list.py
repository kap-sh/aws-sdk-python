"""Generated from Smithy shape ``com.amazonaws.rds#ModifyAdditionalStorageVolumesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.modify_additional_storage_volume

ModifyAdditionalStorageVolumesList: TypeAlias = list[
    "capo_rds.types.modify_additional_storage_volume.ModifyAdditionalStorageVolume"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyAdditionalStorageVolumesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.modify_additional_storage_volume

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.modify_additional_storage_volume.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ModifyAdditionalStorageVolumesList:
    import capo_rds.types.modify_additional_storage_volume

    out: ModifyAdditionalStorageVolumesList = []
    for child in el.findall("member"):
        out.append(
            capo_rds.types.modify_additional_storage_volume.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ModifyAdditionalStorageVolumesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.modify_additional_storage_volume

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.modify_additional_storage_volume.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ModifyAdditionalStorageVolumesList:
    import capo_rds.types.modify_additional_storage_volume

    out: ModifyAdditionalStorageVolumesList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.modify_additional_storage_volume.deserialize_query(child)
        )
    return out
