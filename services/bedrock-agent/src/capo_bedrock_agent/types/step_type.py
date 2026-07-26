"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StepType``."""

from typing import Literal, TypeAlias, cast

StepType: TypeAlias = Literal["POST_CHUNKING",]


# --- restJson1 ser/de ---
def serialize_json(value: StepType) -> str:
    return value


def deserialize_json(data: str) -> StepType:
    return cast(StepType, data)
