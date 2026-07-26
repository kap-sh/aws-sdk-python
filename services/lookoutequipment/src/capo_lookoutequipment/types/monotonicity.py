"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#Monotonicity``."""

from typing import Literal, TypeAlias, cast

Monotonicity: TypeAlias = Literal[
    "DECREASING",
    "INCREASING",
    "STATIC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Monotonicity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Monotonicity:
    return cast(Monotonicity, data)
