"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.image_input

ImageInputs: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.image_input.ImageInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageInputs) -> list:
    import aws_sdk_bedrock_agent_runtime.types.image_input

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.image_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageInputs:
    import aws_sdk_bedrock_agent_runtime.types.image_input

    out: ImageInputs = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.image_input.deserialize_json(item)
        )
    return out
