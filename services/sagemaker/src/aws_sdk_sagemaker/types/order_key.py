"""Generated from Smithy shape ``com.amazonaws.sagemaker#OrderKey``."""

from typing import Literal, TypeAlias, cast

OrderKey: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrderKey:
    return cast(OrderKey, data)
