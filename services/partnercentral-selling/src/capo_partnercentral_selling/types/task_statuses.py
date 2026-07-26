"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TaskStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.task_status

TaskStatuses: TypeAlias = list[
    "capo_partnercentral_selling.types.task_status.TaskStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskStatuses) -> list:
    import capo_partnercentral_selling.types.task_status

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.task_status.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TaskStatuses:
    import capo_partnercentral_selling.types.task_status

    out: TaskStatuses = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.task_status.deserialize_aws_json_1_0(item)
        )
    return out
