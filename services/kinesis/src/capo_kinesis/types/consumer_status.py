"""Generated from Smithy shape ``com.amazonaws.kinesis#ConsumerStatus``."""

from typing import Literal, TypeAlias, cast

ConsumerStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConsumerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConsumerStatus:
    return cast(ConsumerStatus, data)
