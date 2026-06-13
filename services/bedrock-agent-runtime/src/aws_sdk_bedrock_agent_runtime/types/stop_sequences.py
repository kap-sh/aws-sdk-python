"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#StopSequences``."""

from typing import TypeAlias

StopSequences: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StopSequences) -> list:
    return list(value)


def deserialize_json(data: list) -> StopSequences:
    return list(data)
