"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleIdList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.example_id

ExampleIdList: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.example_id.ExampleId"]


# --- restJson1 ser/de ---
def serialize_json(value: ExampleIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExampleIdList:
    return list(data)