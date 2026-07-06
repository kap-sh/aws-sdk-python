"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#BidirectionalInputPayloadPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.part_body


class BidirectionalInputPayloadPart(TypedDict, closed=True):
    bytes: NotRequired["aws_sdk_bedrock_runtime.types.part_body.PartBody"]
    """<p>The audio content for the bidirectional input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BidirectionalInputPayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> BidirectionalInputPayloadPart:
    out: BidirectionalInputPayloadPart = {}  # type: ignore[typeddict-item]
    if "bytes" in data:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.deserialize_json(
            data["bytes"]
        )
    return out


def serialize_event_json(value: BidirectionalInputPayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "chunk"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> BidirectionalInputPayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: BidirectionalInputPayloadPart = {}  # type: ignore[typeddict-item]
    return out
