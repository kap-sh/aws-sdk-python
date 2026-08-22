"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StopSequences``."""

from typing import TypeAlias

StopSequences: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StopSequences) -> list:
    return list(value)


def deserialize_json(data: list) -> StopSequences:
    return [item for item in data if item is not None]
