"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExtractionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The extraction type for a metadata field, determining how the value is obtained during memory processing.</p>"""
ExtractionType: TypeAlias = Literal[
    "LLM_INFERRED",
    "STRICTLY_CONSISTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionType) -> str:
    return value


def deserialize_json(data: str) -> ExtractionType:
    return cast(ExtractionType, data)
