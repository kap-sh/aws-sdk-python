"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcGopBReference``."""

from typing import Literal, TypeAlias, cast

"""Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Don't allow to prevent the encoder from using B-frames as reference frames."""
XavcGopBReference: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: XavcGopBReference) -> str:
    return value


def deserialize_json(data: str) -> XavcGopBReference:
    return cast(XavcGopBReference, data)
