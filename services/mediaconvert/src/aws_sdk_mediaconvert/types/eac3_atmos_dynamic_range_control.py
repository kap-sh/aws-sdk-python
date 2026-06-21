"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosDynamicRangeControl``."""

from typing import Literal, TypeAlias, cast

"""Specify whether MediaConvert should use any dynamic range control metadata from your input file. Keep the default value, Custom, to provide dynamic range control values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your dynamic range control values: Dynamic range compression line and Dynamic range compression RF. When you keep the value Custom for Dynamic range control and you don't specify values for the related settings, MediaConvert uses default values for those settings."""
Eac3AtmosDynamicRangeControl: TypeAlias = Literal[
    "SPECIFIED",
    "INITIALIZE_FROM_SOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosDynamicRangeControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDynamicRangeControl:
    return cast(Eac3AtmosDynamicRangeControl, data)
