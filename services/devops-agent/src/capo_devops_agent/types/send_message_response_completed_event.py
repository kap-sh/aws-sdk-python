"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponseCompletedEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_devops_agent.types.send_message_usage_info


class SendMessageResponseCompletedEvent(TypedDict, closed=True):
    response_id: NotRequired["str"]
    """<p>The response ID</p>"""
    usage: NotRequired[
        "capo_devops_agent.types.send_message_usage_info.SendMessageUsageInfo"
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
        import capo_devops_agent.types.send_message_usage_info

        out["usage"] = capo_devops_agent.types.send_message_usage_info.serialize_json(
            value["usage"]
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageResponseCompletedEvent:
    out: SendMessageResponseCompletedEvent = {}  # type: ignore[typeddict-item]
    if "responseId" in data:
        out["response_id"] = data["responseId"]
    if "usage" in data:
        import capo_devops_agent.types.send_message_usage_info

        out["usage"] = capo_devops_agent.types.send_message_usage_info.deserialize_json(
            data["usage"]
        )
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageResponseCompletedEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "responseCompleted"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageResponseCompletedEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageResponseCompletedEvent = {}  # type: ignore[typeddict-item]
    return out
