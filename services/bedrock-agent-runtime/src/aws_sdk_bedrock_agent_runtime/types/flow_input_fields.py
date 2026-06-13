"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_input_field

FlowInputFields: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.flow_input_field.FlowInputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputFields) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_input_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_input_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FlowInputFields:
    import aws_sdk_bedrock_agent_runtime.types.flow_input_field

    out: FlowInputFields = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_input_field.deserialize_json(item)
        )
    return out
