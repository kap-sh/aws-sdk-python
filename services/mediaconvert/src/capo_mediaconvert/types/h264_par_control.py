"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264ParControl``."""

from typing import Literal, TypeAlias, cast

"""Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings."""
H264ParControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264ParControl) -> str:
    return value


def deserialize_json(data: str) -> H264ParControl:
    return cast(H264ParControl, data)
