"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdIntraCbgProfileClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
XavcHdIntraCbgProfileClass: TypeAlias = Literal[
    "CLASS_50",
    "CLASS_100",
    "CLASS_200",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASS_50",
        "CLASS_100",
        "CLASS_200",
    )
)


def serialize_json(value: XavcHdIntraCbgProfileClass) -> str:
    return value


def deserialize_json(data: str) -> XavcHdIntraCbgProfileClass:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown XavcHdIntraCbgProfileClass value: {data!r}"
        )
    return cast(XavcHdIntraCbgProfileClass, data)
