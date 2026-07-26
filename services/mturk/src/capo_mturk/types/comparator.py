"""Generated from Smithy shape ``com.amazonaws.mturk#Comparator``."""

from typing import Literal, TypeAlias, cast

Comparator: TypeAlias = Literal[
    "LessThan",
    "LessThanOrEqualTo",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "EqualTo",
    "NotEqualTo",
    "Exists",
    "DoesNotExist",
    "In",
    "NotIn",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Comparator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Comparator:
    return cast(Comparator, data)
