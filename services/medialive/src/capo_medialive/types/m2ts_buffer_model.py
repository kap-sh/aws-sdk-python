"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsBufferModel``."""

from typing import Literal, TypeAlias, cast

"""M2ts Buffer Model"""
M2tsBufferModel: TypeAlias = Literal[
    "MULTIPLEX",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsBufferModel) -> str:
    return value


def deserialize_json(data: str) -> M2tsBufferModel:
    return cast(M2tsBufferModel, data)
