"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FailureReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.failure_reason

FailureReasons: TypeAlias = list[
    "capo_bedrock_agent.types.failure_reason.FailureReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureReasons) -> list:
    return list(value)


def deserialize_json(data: list) -> FailureReasons:
    return list(data)
