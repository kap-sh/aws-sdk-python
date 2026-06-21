"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265ParControl``."""

from typing import Literal, TypeAlias, cast

"""Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings."""
H265ParControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265ParControl) -> str:
    return value


def deserialize_json(data: str) -> H265ParControl:
    return cast(H265ParControl, data)
