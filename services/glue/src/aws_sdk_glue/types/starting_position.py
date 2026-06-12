"""Generated from Smithy shape ``com.amazonaws.glue#StartingPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

StartingPosition: TypeAlias = Literal[
    "latest",
    "trim_horizon",
    "earliest",
    "timestamp",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "latest",
        "trim_horizon",
        "earliest",
        "timestamp",
    )
)


def serialize_aws_json_1_1(value: StartingPosition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartingPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StartingPosition value: {data!r}")
    return cast(StartingPosition, data)
