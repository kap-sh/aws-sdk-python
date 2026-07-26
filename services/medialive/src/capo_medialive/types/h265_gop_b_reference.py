"""Generated from Smithy shape ``com.amazonaws.medialive#H265GopBReference``."""

from typing import Literal, TypeAlias, cast

"""H265 Gop BReference"""
H265GopBReference: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265GopBReference) -> str:
    return value


def deserialize_json(data: str) -> H265GopBReference:
    return cast(H265GopBReference, data)
