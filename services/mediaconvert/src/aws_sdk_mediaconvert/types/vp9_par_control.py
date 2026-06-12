"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp9ParControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings."""
Vp9ParControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZE_FROM_SOURCE",
        "SPECIFIED",
    )
)


def serialize_json(value: Vp9ParControl) -> str:
    return value


def deserialize_json(data: str) -> Vp9ParControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vp9ParControl value: {data!r}")
    return cast(Vp9ParControl, data)
