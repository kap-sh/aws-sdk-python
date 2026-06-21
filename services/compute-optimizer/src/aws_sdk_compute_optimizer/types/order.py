"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Order``."""

from typing import Literal, TypeAlias, cast

Order: TypeAlias = Literal[
    "Asc",
    "Desc",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Order) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Order:
    return cast(Order, data)
