"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OutputFiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.output_file

OutputFiles: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.output_file.OutputFile"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFiles) -> list:
    import aws_sdk_bedrock_agent_runtime.types.output_file

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.output_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputFiles:
    import aws_sdk_bedrock_agent_runtime.types.output_file

    out: OutputFiles = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.output_file.deserialize_json(item)
        )
    return out
