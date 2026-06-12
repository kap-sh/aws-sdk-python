"""Generated from Smithy shape ``com.amazonaws.appconfig#ReplicateTo``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

ReplicateTo: TypeAlias = Literal[
    "NONE",
    "SSM_DOCUMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SSM_DOCUMENT",
    )
)


def serialize_json(value: ReplicateTo) -> str:
    return value


def deserialize_json(data: str) -> ReplicateTo:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicateTo value: {data!r}")
    return cast(ReplicateTo, data)
