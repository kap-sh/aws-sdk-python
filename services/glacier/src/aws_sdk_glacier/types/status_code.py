"""Generated from Smithy shape ``com.amazonaws.glacier#StatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

StatusCode: TypeAlias = Literal[
    "InProgress",
    "Succeeded",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Succeeded",
        "Failed",
    )
)


def serialize_json(value: StatusCode) -> str:
    return value


def deserialize_json(data: str) -> StatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusCode value: {data!r}")
    return cast(StatusCode, data)
