"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsBufferModel``."""

from typing import Literal, TypeAlias, cast

"""Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions."""
M2tsBufferModel: TypeAlias = Literal[
    "MULTIPLEX",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsBufferModel) -> str:
    return value


def deserialize_json(data: str) -> M2tsBufferModel:
    return cast(M2tsBufferModel, data)
