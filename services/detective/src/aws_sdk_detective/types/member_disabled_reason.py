"""Generated from Smithy shape ``com.amazonaws.detective#MemberDisabledReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

MemberDisabledReason: TypeAlias = Literal[
    "VOLUME_TOO_HIGH",
    "VOLUME_UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOLUME_TOO_HIGH",
        "VOLUME_UNKNOWN",
    )
)


def serialize_json(value: MemberDisabledReason) -> str:
    return value


def deserialize_json(data: str) -> MemberDisabledReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberDisabledReason value: {data!r}")
    return cast(MemberDisabledReason, data)
