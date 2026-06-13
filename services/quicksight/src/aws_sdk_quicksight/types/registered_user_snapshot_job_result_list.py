"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserSnapshotJobResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.registered_user_snapshot_job_result

RegisteredUserSnapshotJobResultList: TypeAlias = list[
    "aws_sdk_quicksight.types.registered_user_snapshot_job_result.RegisteredUserSnapshotJobResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserSnapshotJobResultList) -> list:
    import aws_sdk_quicksight.types.registered_user_snapshot_job_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.registered_user_snapshot_job_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegisteredUserSnapshotJobResultList:
    import aws_sdk_quicksight.types.registered_user_snapshot_job_result

    out: RegisteredUserSnapshotJobResultList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.registered_user_snapshot_job_result.deserialize_json(
                item
            )
        )
    return out
