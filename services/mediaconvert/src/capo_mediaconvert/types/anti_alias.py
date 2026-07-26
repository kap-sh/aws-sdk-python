"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AntiAlias``."""

from typing import Literal, TypeAlias, cast

"""The anti-alias filter is automatically applied to all outputs. The service no longer accepts the value DISABLED for AntiAlias. If you specify that in your job, the service will ignore the setting."""
AntiAlias: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AntiAlias) -> str:
    return value


def deserialize_json(data: str) -> AntiAlias:
    return cast(AntiAlias, data)
