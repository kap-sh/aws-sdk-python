"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp8ParControl``."""

from typing import Literal, TypeAlias, cast

"""Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings."""
Vp8ParControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Vp8ParControl) -> str:
    return value


def deserialize_json(data: str) -> Vp8ParControl:
    return cast(Vp8ParControl, data)
