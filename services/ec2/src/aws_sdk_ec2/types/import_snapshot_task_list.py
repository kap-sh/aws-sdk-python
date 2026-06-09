"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_snapshot_task

ImportSnapshotTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.import_snapshot_task.ImportSnapshotTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportSnapshotTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.import_snapshot_task

        aws_sdk_ec2.types.import_snapshot_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ImportSnapshotTaskList:
    import aws_sdk_ec2.types.import_snapshot_task

    out: ImportSnapshotTaskList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.import_snapshot_task.deserialize_ec2_query(child))
    return out
