"""Generated from Smithy shape ``com.amazonaws.appflow#AggregationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

AggregationType: TypeAlias = Literal[
    "None",
    "SingleFile",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "SingleFile",
    )
)


def serialize_json(value: AggregationType) -> str:
    return value


def deserialize_json(data: str) -> AggregationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregationType value: {data!r}")
    return cast(AggregationType, data)
