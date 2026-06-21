"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EmbeddedTerminateCaptions``."""

from typing import Literal, TypeAlias, cast

"""By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting."""
EmbeddedTerminateCaptions: TypeAlias = Literal[
    "END_OF_INPUT",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedTerminateCaptions) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedTerminateCaptions:
    return cast(EmbeddedTerminateCaptions, data)
