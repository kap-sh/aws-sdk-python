"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessReasoningContentBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.body


class _HarnessReasoningContentBlockDelta_text(TypedDict, closed=True):
    text: "str"


class _HarnessReasoningContentBlockDelta_redactedContent(TypedDict, closed=True):
    redactedContent: "capo_bedrock_agentcore.types.body.Body"


class _HarnessReasoningContentBlockDelta_signature(TypedDict, closed=True):
    signature: "str"


HarnessReasoningContentBlockDelta: TypeAlias = (
    _HarnessReasoningContentBlockDelta_text
    | _HarnessReasoningContentBlockDelta_redactedContent
    | _HarnessReasoningContentBlockDelta_signature
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessReasoningContentBlockDelta) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "redactedContent" in value:
        import capo_bedrock_agentcore.types.body

        return {
            "redactedContent": capo_bedrock_agentcore.types.body.serialize_json(
                value["redactedContent"]
            )
        }
    elif "signature" in value:
        return {"signature": value["signature"]}
    else:
        raise SerializationError(
            "HarnessReasoningContentBlockDelta: no variant present"
        )


def deserialize_json(data: dict) -> HarnessReasoningContentBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("redactedContent") is not None:
        import capo_bedrock_agentcore.types.body

        return {
            "redactedContent": capo_bedrock_agentcore.types.body.deserialize_json(
                data["redactedContent"]
            )
        }
    elif data.get("signature") is not None:
        return {"signature": data["signature"]}
    else:
        raise DeserializationError(
            "HarnessReasoningContentBlockDelta: no recognized variant key"
        )
