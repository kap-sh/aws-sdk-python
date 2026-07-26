"""Generated from Smithy shape ``com.amazonaws.kendra#Order``."""

from typing import Literal, TypeAlias, cast

Order: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Order) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Order:
    return cast(Order, data)
