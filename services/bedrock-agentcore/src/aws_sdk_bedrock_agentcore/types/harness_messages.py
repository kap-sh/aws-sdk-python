"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_message

HarnessMessages: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.harness_message.HarnessMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMessages) -> list:
    import aws_sdk_bedrock_agentcore.types.harness_message

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.harness_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> HarnessMessages:
    import aws_sdk_bedrock_agentcore.types.harness_message

    out: HarnessMessages = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.harness_message.deserialize_json(item)
        )
    return out
