"""Generated from Smithy shape ``com.amazonaws.mturk#NotifyWorkersFailureStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.notify_workers_failure_status

NotifyWorkersFailureStatusList: TypeAlias = list[
    "aws_sdk_mturk.types.notify_workers_failure_status.NotifyWorkersFailureStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyWorkersFailureStatusList) -> list:
    import aws_sdk_mturk.types.notify_workers_failure_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mturk.types.notify_workers_failure_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotifyWorkersFailureStatusList:
    import aws_sdk_mturk.types.notify_workers_failure_status

    out: NotifyWorkersFailureStatusList = []
    for item in data:
        out.append(
            aws_sdk_mturk.types.notify_workers_failure_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
