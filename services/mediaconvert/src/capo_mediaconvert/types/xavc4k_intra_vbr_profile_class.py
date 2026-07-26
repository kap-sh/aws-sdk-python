"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kIntraVbrProfileClass``."""

from typing import Literal, TypeAlias, cast

"""Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
Xavc4kIntraVbrProfileClass: TypeAlias = Literal[
    "CLASS_100",
    "CLASS_300",
    "CLASS_480",
]


# --- restJson1 ser/de ---
def serialize_json(value: Xavc4kIntraVbrProfileClass) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kIntraVbrProfileClass:
    return cast(Xavc4kIntraVbrProfileClass, data)
