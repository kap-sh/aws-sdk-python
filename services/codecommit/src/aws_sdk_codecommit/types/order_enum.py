"""Generated from Smithy shape ``com.amazonaws.codecommit#OrderEnum``."""

from typing import Literal, TypeAlias, cast

OrderEnum: TypeAlias = Literal[
    "ascending",
    "descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrderEnum:
    return cast(OrderEnum, data)
