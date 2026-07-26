"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#PayloadPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.part_body


class PayloadPart(TypedDict, closed=True):
    bytes: NotRequired["capo_bedrock_runtime.types.part_body.PartBody"]
    """<p>Base64-encoded bytes of payload data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import capo_bedrock_runtime.types.part_body

        out["bytes"] = capo_bedrock_runtime.types.part_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> PayloadPart:
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    if "bytes" in data:
        import capo_bedrock_runtime.types.part_body

        out["bytes"] = capo_bedrock_runtime.types.part_body.deserialize_json(
            data["bytes"]
        )
    return out


def serialize_event_json(value: PayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "chunk"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> PayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    return out
