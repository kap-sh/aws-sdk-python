"""Generated from Smithy shape ``com.amazonaws.rds#AdditionalStorageVolumesOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.additional_storage_volume_output

AdditionalStorageVolumesOutputList: TypeAlias = list[
    "aws_sdk_rds.types.additional_storage_volume_output.AdditionalStorageVolumeOutput"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AdditionalStorageVolumesOutputList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.additional_storage_volume_output

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.additional_storage_volume_output.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AdditionalStorageVolumesOutputList:
    import aws_sdk_rds.types.additional_storage_volume_output

    out: AdditionalStorageVolumesOutputList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_rds.types.additional_storage_volume_output.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AdditionalStorageVolumesOutputList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.additional_storage_volume_output

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.additional_storage_volume_output.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> AdditionalStorageVolumesOutputList:
    import aws_sdk_rds.types.additional_storage_volume_output

    out: AdditionalStorageVolumesOutputList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.additional_storage_volume_output.deserialize_query(child)
        )
    return out
