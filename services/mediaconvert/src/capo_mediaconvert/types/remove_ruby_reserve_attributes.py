"""Generated from Smithy shape ``com.amazonaws.mediaconvert#RemoveRubyReserveAttributes``."""

from typing import Literal, TypeAlias, cast

"""Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled."""
RemoveRubyReserveAttributes: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoveRubyReserveAttributes) -> str:
    return value


def deserialize_json(data: str) -> RemoveRubyReserveAttributes:
    return cast(RemoveRubyReserveAttributes, data)
