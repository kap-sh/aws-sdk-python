"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ImscStylePassthrough``."""

from typing import Literal, TypeAlias, cast

"""Keep this setting enabled to have MediaConvert use the font style and position information from the captions source in the output. This option is available only when your input captions are IMSC, SMPTE-TT, or TTML. Disable this setting for simplified output captions."""
ImscStylePassthrough: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImscStylePassthrough) -> str:
    return value


def deserialize_json(data: str) -> ImscStylePassthrough:
    return cast(ImscStylePassthrough, data)
