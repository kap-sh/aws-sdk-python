"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponseCompletedEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.send_message_usage_info


class SendMessageResponseCompletedEvent(TypedDict):
    response_id: NotRequired["str"]
    """<p>The response ID</p>"""
    usage: NotRequired[
        "aws_sdk_devops_agent.types.send_message_usage_info.SendMessageUsageInfo"
    ]
    """<p>Token usage information</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponseCompletedEvent) -> dict:
    out: dict = {}
    if "response_id" in value:
        out["responseId"] = value["response_id"]
    if "usage" in value:
        import aws_sdk_devops_agent.types.send_message_usage_info

        out["usage"] = (
            aws_sdk_devops_agent.types.send_message_usage_info.serialize_json(
                value["usage"]
            )
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageResponseCompletedEvent:
    out: SendMessageResponseCompletedEvent = {}  # type: ignore[typeddict-item]
    if "responseId" in data:
        out["response_id"] = data["responseId"]
    if "usage" in data:
        import aws_sdk_devops_agent.types.send_message_usage_info

        out["usage"] = (
            aws_sdk_devops_agent.types.send_message_usage_info.deserialize_json(
                data["usage"]
            )
        )
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out
