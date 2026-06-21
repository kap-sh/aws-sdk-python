"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#PIIRedactionMaskMode``."""

from typing import Literal, TypeAlias, cast

"""Mode for redacting detected PII"""
PIIRedactionMaskMode: TypeAlias = Literal[
    "PII",
    "ENTITY_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PIIRedactionMaskMode) -> str:
    return value


def deserialize_json(data: str) -> PIIRedactionMaskMode:
    return cast(PIIRedactionMaskMode, data)
