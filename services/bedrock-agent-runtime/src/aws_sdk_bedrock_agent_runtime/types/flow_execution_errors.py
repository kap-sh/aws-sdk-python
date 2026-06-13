"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_error

FlowExecutionErrors: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.flow_execution_error.FlowExecutionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionErrors) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_execution_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowExecutionErrors:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_error

    out: FlowExecutionErrors = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_execution_error.deserialize_json(
                item
            )
        )
    return out
