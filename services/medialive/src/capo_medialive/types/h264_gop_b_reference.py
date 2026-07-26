"""Generated from Smithy shape ``com.amazonaws.medialive#H264GopBReference``."""

from typing import Literal, TypeAlias, cast

"""H264 Gop BReference"""
H264GopBReference: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264GopBReference) -> str:
    return value


def deserialize_json(data: str) -> H264GopBReference:
    return cast(H264GopBReference, data)
