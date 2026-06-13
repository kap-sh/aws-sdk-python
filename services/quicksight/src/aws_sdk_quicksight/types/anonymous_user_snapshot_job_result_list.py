"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserSnapshotJobResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.anonymous_user_snapshot_job_result

AnonymousUserSnapshotJobResultList: TypeAlias = list[
    "aws_sdk_quicksight.types.anonymous_user_snapshot_job_result.AnonymousUserSnapshotJobResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnonymousUserSnapshotJobResultList) -> list:
    import aws_sdk_quicksight.types.anonymous_user_snapshot_job_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.anonymous_user_snapshot_job_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnonymousUserSnapshotJobResultList:
    import aws_sdk_quicksight.types.anonymous_user_snapshot_job_result

    out: AnonymousUserSnapshotJobResultList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.anonymous_user_snapshot_job_result.deserialize_json(
                item
            )
        )
    return out
