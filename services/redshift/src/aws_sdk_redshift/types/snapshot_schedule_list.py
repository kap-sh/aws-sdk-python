"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot_schedule

SnapshotScheduleList: TypeAlias = list[
    "aws_sdk_redshift.types.snapshot_schedule.SnapshotSchedule"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotScheduleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.snapshot_schedule

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.snapshot_schedule.serialize_query(
            item, pairs, f"{prefix}.SnapshotSchedule.{n}"
        )


def deserialize_query(el: Element) -> SnapshotScheduleList:
    import aws_sdk_redshift.types.snapshot_schedule

    out: SnapshotScheduleList = []
    for child in el.findall("SnapshotSchedule"):
        out.append(aws_sdk_redshift.types.snapshot_schedule.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SnapshotScheduleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.snapshot_schedule

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.snapshot_schedule.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SnapshotScheduleList:
    import aws_sdk_redshift.types.snapshot_schedule

    out: SnapshotScheduleList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.snapshot_schedule.deserialize_query(child))
    return out
