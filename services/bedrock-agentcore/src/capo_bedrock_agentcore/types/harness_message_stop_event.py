"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMessageStopEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_stop_reason


class HarnessMessageStopEvent(TypedDict, closed=True):
    stop_reason: "capo_bedrock_agentcore.types.harness_stop_reason.HarnessStopReason"
    """<p>The reason the agent stopped generating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMessageStopEvent) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.harness_stop_reason

    out["stopReason"] = capo_bedrock_agentcore.types.harness_stop_reason.serialize_json(
        value["stop_reason"]
    )
    return out


def deserialize_json(data: dict) -> HarnessMessageStopEvent:
    out: HarnessMessageStopEvent = {}  # type: ignore[typeddict-item]
    if "stopReason" in data:
        import capo_bedrock_agentcore.types.harness_stop_reason

        out["stop_reason"] = (
            capo_bedrock_agentcore.types.harness_stop_reason.deserialize_json(
                data["stopReason"]
            )
        )
    else:
        raise DeserializationError("HarnessMessageStopEvent.stop_reason required")
    return out


def serialize_event_json(value: HarnessMessageStopEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "messageStop"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> HarnessMessageStopEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HarnessMessageStopEvent = {}  # type: ignore[typeddict-item]
    return out
