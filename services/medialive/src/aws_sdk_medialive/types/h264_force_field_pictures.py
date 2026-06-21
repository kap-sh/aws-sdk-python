"""Generated from Smithy shape ``com.amazonaws.medialive#H264ForceFieldPictures``."""

from typing import Literal, TypeAlias, cast

"""H264 Force Field Pictures"""
H264ForceFieldPictures: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264ForceFieldPictures) -> str:
    return value


def deserialize_json(data: str) -> H264ForceFieldPictures:
    return cast(H264ForceFieldPictures, data)
