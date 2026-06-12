"""Generated from Smithy shape ``com.amazonaws.gamelift#QueueArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.arn_string_model

QueueArnsList: TypeAlias = list[
    "aws_sdk_gamelift.types.arn_string_model.ArnStringModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueArnsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> QueueArnsList:
    return list(data)
