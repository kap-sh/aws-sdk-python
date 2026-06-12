"""Generated from Smithy shape ``com.amazonaws.connect#RehydrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RehydrationType: TypeAlias = Literal[
    "ENTIRE_PAST_SESSION",
    "FROM_SEGMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENTIRE_PAST_SESSION",
        "FROM_SEGMENT",
    )
)


def serialize_json(value: RehydrationType) -> str:
    return value


def deserialize_json(data: str) -> RehydrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RehydrationType value: {data!r}")
    return cast(RehydrationType, data)
