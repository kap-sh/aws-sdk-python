"""Generated from Smithy shape ``com.amazonaws.forecast#Operation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

Operation: TypeAlias = Literal[
    "ADD",
    "SUBTRACT",
    "MULTIPLY",
    "DIVIDE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "SUBTRACT",
        "MULTIPLY",
        "DIVIDE",
    )
)


def serialize_aws_json_1_1(value: Operation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Operation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operation value: {data!r}")
    return cast(Operation, data)
