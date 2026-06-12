"""Generated from Smithy shape ``com.amazonaws.rds#ModifyAdditionalStorageVolumesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.modify_additional_storage_volume

ModifyAdditionalStorageVolumesList: TypeAlias = list[
    "aws_sdk_rds.types.modify_additional_storage_volume.ModifyAdditionalStorageVolume"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyAdditionalStorageVolumesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.modify_additional_storage_volume

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.modify_additional_storage_volume.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ModifyAdditionalStorageVolumesList:
    import aws_sdk_rds.types.modify_additional_storage_volume

    out: ModifyAdditionalStorageVolumesList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_rds.types.modify_additional_storage_volume.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ModifyAdditionalStorageVolumesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.modify_additional_storage_volume

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.modify_additional_storage_volume.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ModifyAdditionalStorageVolumesList:
    import aws_sdk_rds.types.modify_additional_storage_volume

    out: ModifyAdditionalStorageVolumesList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.modify_additional_storage_volume.deserialize_query(child)
        )
    return out
