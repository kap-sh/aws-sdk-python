"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AdditionalModelResponseFieldPaths``."""

from typing import TypeAlias

AdditionalModelResponseFieldPaths: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalModelResponseFieldPaths) -> list:
    return list(value)


def deserialize_json(data: list) -> AdditionalModelResponseFieldPaths:
    return list(data)