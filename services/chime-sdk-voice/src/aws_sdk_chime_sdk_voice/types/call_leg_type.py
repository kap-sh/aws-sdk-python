"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CallLegType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

CallLegType: TypeAlias = Literal[
    "Caller",
    "Callee",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Caller",
        "Callee",
    )
)


def serialize_json(value: CallLegType) -> str:
    return value


def deserialize_json(data: str) -> CallLegType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CallLegType value: {data!r}")
    return cast(CallLegType, data)
