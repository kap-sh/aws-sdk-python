"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMessageStartEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_conversation_role


class HarnessMessageStartEvent(TypedDict):
    role: "aws_sdk_bedrock_agentcore.types.harness_conversation_role.HarnessConversationRole"
    """<p>The role of the message sender.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMessageStartEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.harness_conversation_role

    out["role"] = (
        aws_sdk_bedrock_agentcore.types.harness_conversation_role.serialize_json(
            value["role"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessMessageStartEvent:
    out: HarnessMessageStartEvent = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import aws_sdk_bedrock_agentcore.types.harness_conversation_role

        out["role"] = (
            aws_sdk_bedrock_agentcore.types.harness_conversation_role.deserialize_json(
                data["role"]
            )
        )
    else:
        raise DeserializationError("HarnessMessageStartEvent.role required")
    return out
