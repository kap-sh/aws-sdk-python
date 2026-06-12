"""Generated from Smithy shape ``com.amazonaws.amplify#Platform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

Platform: TypeAlias = Literal[
    "WEB",
    "WEB_DYNAMIC",
    "WEB_COMPUTE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WEB",
        "WEB_DYNAMIC",
        "WEB_COMPUTE",
    )
)


def serialize_json(value: Platform) -> str:
    return value


def deserialize_json(data: str) -> Platform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Platform value: {data!r}")
    return cast(Platform, data)
