"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kIntraVbrProfileClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
Xavc4kIntraVbrProfileClass: TypeAlias = Literal[
    "CLASS_100",
    "CLASS_300",
    "CLASS_480",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASS_100",
        "CLASS_300",
        "CLASS_480",
    )
)


def serialize_json(value: Xavc4kIntraVbrProfileClass) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kIntraVbrProfileClass:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Xavc4kIntraVbrProfileClass value: {data!r}"
        )
    return cast(Xavc4kIntraVbrProfileClass, data)
