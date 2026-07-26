"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosDownmixControl``."""

from typing import Literal, TypeAlias, cast

"""Specify whether MediaConvert should use any downmix metadata from your input file. Keep the default value, Custom to provide downmix values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your downmix values: Left only/Right only surround, Left total/Right total surround, Left total/Right total center, Left only/Right only center, and Stereo downmix. When you keep Custom for Downmix control and you don't specify values for the related settings, MediaConvert uses default values for those settings."""
Eac3AtmosDownmixControl: TypeAlias = Literal[
    "SPECIFIED",
    "INITIALIZE_FROM_SOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosDownmixControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDownmixControl:
    return cast(Eac3AtmosDownmixControl, data)
