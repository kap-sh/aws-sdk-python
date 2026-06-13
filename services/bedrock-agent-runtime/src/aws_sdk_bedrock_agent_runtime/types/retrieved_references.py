"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievedReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieved_reference

RetrievedReferences: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.retrieved_reference.RetrievedReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedReferences) -> list:
    import aws_sdk_bedrock_agent_runtime.types.retrieved_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.retrieved_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetrievedReferences:
    import aws_sdk_bedrock_agent_runtime.types.retrieved_reference

    out: RetrievedReferences = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.retrieved_reference.deserialize_json(
                item
            )
        )
    return out
