"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3PassthroughControl``."""

from typing import Literal, TypeAlias, cast

"""When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding."""
Eac3PassthroughControl: TypeAlias = Literal[
    "WHEN_POSSIBLE",
    "NO_PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3PassthroughControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3PassthroughControl:
    return cast(Eac3PassthroughControl, data)
