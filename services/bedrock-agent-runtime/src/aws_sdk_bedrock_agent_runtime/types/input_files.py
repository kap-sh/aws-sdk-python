"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputFiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.input_file

InputFiles: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.input_file.InputFile"]


# --- restJson1 ser/de ---
def serialize_json(value: InputFiles) -> list:
    import aws_sdk_bedrock_agent_runtime.types.input_file

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.input_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputFiles:
    import aws_sdk_bedrock_agent_runtime.types.input_file

    out: InputFiles = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.input_file.deserialize_json(item)
        )
    return out
