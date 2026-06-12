"""Generated from Smithy shape ``com.amazonaws.glue#Comparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

Comparator: TypeAlias = Literal[
    "EQUALS",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_EQUALS",
    "LESS_THAN_EQUALS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_THAN_EQUALS",
        "LESS_THAN_EQUALS",
    )
)


def serialize_aws_json_1_1(value: Comparator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Comparator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Comparator value: {data!r}")
    return cast(Comparator, data)
