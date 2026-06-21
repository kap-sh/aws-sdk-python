"""Generated from Smithy shape ``com.amazonaws.medialive#H265SubGopLength``."""

from typing import Literal, TypeAlias, cast

"""H265 Sub Gop Length"""
H265SubGopLength: TypeAlias = Literal[
    "DYNAMIC",
    "FIXED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265SubGopLength) -> str:
    return value


def deserialize_json(data: str) -> H265SubGopLength:
    return cast(H265SubGopLength, data)
