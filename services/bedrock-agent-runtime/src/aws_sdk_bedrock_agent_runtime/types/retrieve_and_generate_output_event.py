"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateOutputEvent``."""

from typing import TypedDict

from aws_sdk_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError


class RetrieveAndGenerateOutputEvent(TypedDict):
    text: "str"
    """<p>A text response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateOutputEvent) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateOutputEvent:
    out: RetrieveAndGenerateOutputEvent = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("RetrieveAndGenerateOutputEvent.text required")
    return out


def serialize_event_json(value: RetrieveAndGenerateOutputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "output"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> RetrieveAndGenerateOutputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: RetrieveAndGenerateOutputEvent = {}  # type: ignore[typeddict-item]
    return out
