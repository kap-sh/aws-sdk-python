"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RangeMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

RangeMode: TypeAlias = Literal[
    "FIRST",
    "LAST",
    "LAST_BEFORE_MISSING_VALUES",
    "INCLUSIVE",
    "EXCLUSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIRST",
        "LAST",
        "LAST_BEFORE_MISSING_VALUES",
        "INCLUSIVE",
        "EXCLUSIVE",
    )
)


def serialize_json(value: RangeMode) -> str:
    return value


def deserialize_json(data: str) -> RangeMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RangeMode value: {data!r}")
    return cast(RangeMode, data)
