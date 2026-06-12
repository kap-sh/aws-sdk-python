"""Generated from Smithy shape ``com.amazonaws.connect#ResponseMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ResponseMode: TypeAlias = Literal[
    "INCREMENTAL",
    "COMPLETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCREMENTAL",
        "COMPLETE",
    )
)


def serialize_json(value: ResponseMode) -> str:
    return value


def deserialize_json(data: str) -> ResponseMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponseMode value: {data!r}")
    return cast(ResponseMode, data)
