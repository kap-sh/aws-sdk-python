"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Platform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

Platform: TypeAlias = Literal[
    "Windows",
    "Linux",
    "macOS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Windows",
        "Linux",
        "macOS",
    )
)


def serialize_json(value: Platform) -> str:
    return value


def deserialize_json(data: str) -> Platform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Platform value: {data!r}")
    return cast(Platform, data)
