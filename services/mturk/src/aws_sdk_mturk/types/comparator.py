"""Generated from Smithy shape ``com.amazonaws.mturk#Comparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: Comparator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Comparator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Comparator value: {data!r}")
    return cast(Comparator, data)
