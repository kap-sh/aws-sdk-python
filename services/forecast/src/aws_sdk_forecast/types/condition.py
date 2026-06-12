"""Generated from Smithy shape ``com.amazonaws.forecast#Condition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

Condition: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "LESS_THAN",
    "GREATER_THAN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
        "LESS_THAN",
        "GREATER_THAN",
    )
)


def serialize_aws_json_1_1(value: Condition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Condition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Condition value: {data!r}")
    return cast(Condition, data)
