"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobS3ResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_job_s3_result

SnapshotJobS3ResultList: TypeAlias = list[
    "aws_sdk_quicksight.types.snapshot_job_s3_result.SnapshotJobS3Result"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobS3ResultList) -> list:
    import aws_sdk_quicksight.types.snapshot_job_s3_result

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.snapshot_job_s3_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SnapshotJobS3ResultList:
    import aws_sdk_quicksight.types.snapshot_job_s3_result

    out: SnapshotJobS3ResultList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.snapshot_job_s3_result.deserialize_json(item)
        )
    return out
