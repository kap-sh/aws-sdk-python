"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseSnapshotInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.database_snapshot_info

DatabaseSnapshotInfoList: TypeAlias = list[
    "aws_sdk_firehose.types.database_snapshot_info.DatabaseSnapshotInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseSnapshotInfoList) -> list:
    import aws_sdk_firehose.types.database_snapshot_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_firehose.types.database_snapshot_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatabaseSnapshotInfoList:
    import aws_sdk_firehose.types.database_snapshot_info

    out: DatabaseSnapshotInfoList = []
    for item in data:
        out.append(
            aws_sdk_firehose.types.database_snapshot_info.deserialize_aws_json_1_1(item)
        )
    return out
