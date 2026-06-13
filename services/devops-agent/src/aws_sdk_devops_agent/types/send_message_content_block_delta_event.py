"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContentBlockDeltaEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.send_message_content_block_delta


class SendMessageContentBlockDeltaEvent(TypedDict):
    index: NotRequired["int"]
    """<p>Zero-based index of the content block</p>"""
    delta: NotRequired[
        "aws_sdk_devops_agent.types.send_message_content_block_delta.SendMessageContentBlockDelta"
    ]
    """<p>The incremental content delta</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContentBlockDeltaEvent) -> dict:
    out: dict = {}
    if "index" in value:
        out["index"] = value["index"]
    if "delta" in value:
        import aws_sdk_devops_agent.types.send_message_content_block_delta

        out["delta"] = (
            aws_sdk_devops_agent.types.send_message_content_block_delta.serialize_json(
                value["delta"]
            )
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageContentBlockDeltaEvent:
    out: SendMessageContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if "index" in data:
        out["index"] = data["index"]
    if "delta" in data:
        import aws_sdk_devops_agent.types.send_message_content_block_delta

        out["delta"] = (
            aws_sdk_devops_agent.types.send_message_content_block_delta.deserialize_json(
                data["delta"]
            )
        )
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out
