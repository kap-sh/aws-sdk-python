"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.image_input

ImageInputs: TypeAlias = list["capo_bedrock_agent_runtime.types.image_input.ImageInput"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageInputs) -> list:
    import capo_bedrock_agent_runtime.types.image_input

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.image_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageInputs:
    import capo_bedrock_agent_runtime.types.image_input

    out: ImageInputs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.image_input.deserialize_json(item))
    return out
