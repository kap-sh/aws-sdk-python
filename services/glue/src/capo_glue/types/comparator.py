"""Generated from Smithy shape ``com.amazonaws.glue#Comparator``."""

from typing import Literal, TypeAlias, cast

Comparator: TypeAlias = Literal[
    "EQUALS",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_EQUALS",
    "LESS_THAN_EQUALS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Comparator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Comparator:
    return cast(Comparator, data)
