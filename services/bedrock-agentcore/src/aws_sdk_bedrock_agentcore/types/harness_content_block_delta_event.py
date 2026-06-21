"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockDeltaEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_content_block_delta


class HarnessContentBlockDeltaEvent(TypedDict):
    content_block_index: "int"
    """<p>The index of the content block being updated.</p>"""
    delta: "aws_sdk_bedrock_agentcore.types.harness_content_block_delta.HarnessContentBlockDelta"
    """<p>The delta payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockDeltaEvent) -> dict:
    out: dict = {}
    out["contentBlockIndex"] = value["content_block_index"]
    import aws_sdk_bedrock_agentcore.types.harness_content_block_delta

    out["delta"] = (
        aws_sdk_bedrock_agentcore.types.harness_content_block_delta.serialize_json(
            value["delta"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessContentBlockDeltaEvent:
    out: HarnessContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if "contentBlockIndex" in data:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "HarnessContentBlockDeltaEvent.content_block_index required"
        )
    if "delta" in data:
        import aws_sdk_bedrock_agentcore.types.harness_content_block_delta

        out["delta"] = (
            aws_sdk_bedrock_agentcore.types.harness_content_block_delta.deserialize_json(
                data["delta"]
            )
        )
    else:
        raise DeserializationError("HarnessContentBlockDeltaEvent.delta required")
    return out


def serialize_event_json(value: HarnessContentBlockDeltaEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "contentBlockDelta"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> HarnessContentBlockDeltaEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HarnessContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    return out
