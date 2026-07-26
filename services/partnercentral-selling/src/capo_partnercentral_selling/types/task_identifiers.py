"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TaskIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.task_arn_or_identifier

TaskIdentifiers: TypeAlias = list[
    "capo_partnercentral_selling.types.task_arn_or_identifier.TaskArnOrIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TaskIdentifiers:
    return list(data)
