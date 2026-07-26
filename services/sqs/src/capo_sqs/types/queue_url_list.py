"""Generated from Smithy shape ``com.amazonaws.sqs#QueueUrlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.string

QueueUrlList: TypeAlias = list["capo_sqs.types.string.String"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueueUrlList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> QueueUrlList:
    return list(data)
