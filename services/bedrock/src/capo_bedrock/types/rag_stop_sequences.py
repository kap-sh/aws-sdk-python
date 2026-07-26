"""Generated from Smithy shape ``com.amazonaws.bedrock#RAGStopSequences``."""

from typing import TypeAlias

RAGStopSequences: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RAGStopSequences) -> list:
    return list(value)


def deserialize_json(data: list) -> RAGStopSequences:
    return list(data)
