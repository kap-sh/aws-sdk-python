"""Generated from Smithy shape ``com.amazonaws.forecast#Condition``."""

from typing import Literal, TypeAlias, cast

Condition: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "LESS_THAN",
    "GREATER_THAN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Condition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Condition:
    return cast(Condition, data)
