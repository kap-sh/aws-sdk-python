"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdIntraCbgProfileClass``."""

from typing import Literal, TypeAlias, cast

"""Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
XavcHdIntraCbgProfileClass: TypeAlias = Literal[
    "CLASS_50",
    "CLASS_100",
    "CLASS_200",
]


# --- restJson1 ser/de ---
def serialize_json(value: XavcHdIntraCbgProfileClass) -> str:
    return value


def deserialize_json(data: str) -> XavcHdIntraCbgProfileClass:
    return cast(XavcHdIntraCbgProfileClass, data)
