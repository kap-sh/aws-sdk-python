"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kIntraCbgProfileClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the XAVC Intra 4k (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
Xavc4kIntraCbgProfileClass: TypeAlias = Literal[
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


def serialize_json(value: Xavc4kIntraCbgProfileClass) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kIntraCbgProfileClass:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Xavc4kIntraCbgProfileClass value: {data!r}"
        )
    return cast(Xavc4kIntraCbgProfileClass, data)
