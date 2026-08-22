"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.example_id

ExampleIdList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.example_id.ExampleId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExampleIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExampleIdList:
    return [item for item in data if item is not None]
