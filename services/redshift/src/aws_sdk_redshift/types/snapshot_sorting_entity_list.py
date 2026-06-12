"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotSortingEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot_sorting_entity

SnapshotSortingEntityList: TypeAlias = list[
    "aws_sdk_redshift.types.snapshot_sorting_entity.SnapshotSortingEntity"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotSortingEntityList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.snapshot_sorting_entity

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.snapshot_sorting_entity.serialize_query(
            item, pairs, f"{prefix}.SnapshotSortingEntity.{n}"
        )


def deserialize_query(el: Element) -> SnapshotSortingEntityList:
    import aws_sdk_redshift.types.snapshot_sorting_entity

    out: SnapshotSortingEntityList = []
    for child in el.findall("SnapshotSortingEntity"):
        out.append(
            aws_sdk_redshift.types.snapshot_sorting_entity.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: SnapshotSortingEntityList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.snapshot_sorting_entity

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.snapshot_sorting_entity.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SnapshotSortingEntityList:
    import aws_sdk_redshift.types.snapshot_sorting_entity

    out: SnapshotSortingEntityList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.snapshot_sorting_entity.deserialize_query(child)
        )
    return out
