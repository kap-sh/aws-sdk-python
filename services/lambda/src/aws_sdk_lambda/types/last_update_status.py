"""Generated from Smithy shape ``com.amazonaws.lambda#LastUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

LastUpdateStatus: TypeAlias = Literal[
    "Successful",
    "Failed",
    "InProgress",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Successful",
        "Failed",
        "InProgress",
    )
)


def serialize_json(value: LastUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> LastUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastUpdateStatus value: {data!r}")
    return cast(LastUpdateStatus, data)
