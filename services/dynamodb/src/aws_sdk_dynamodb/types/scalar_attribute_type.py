"""Generated from Smithy shape ``com.amazonaws.dynamodb#ScalarAttributeType``."""

from typing import Literal, TypeAlias, cast

ScalarAttributeType: TypeAlias = Literal[
    "S",
    "N",
    "B",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScalarAttributeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScalarAttributeType:
    return cast(ScalarAttributeType, data)
