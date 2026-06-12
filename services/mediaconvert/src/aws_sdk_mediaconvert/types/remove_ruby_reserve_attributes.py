"""Generated from Smithy shape ``com.amazonaws.mediaconvert#RemoveRubyReserveAttributes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled."""
RemoveRubyReserveAttributes: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: RemoveRubyReserveAttributes) -> str:
    return value


def deserialize_json(data: str) -> RemoveRubyReserveAttributes:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RemoveRubyReserveAttributes value: {data!r}"
        )
    return cast(RemoveRubyReserveAttributes, data)
