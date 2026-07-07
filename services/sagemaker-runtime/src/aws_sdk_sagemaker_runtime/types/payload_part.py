"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#PayloadPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.part_blob


class PayloadPart(TypedDict, closed=True):
    bytes: NotRequired["aws_sdk_sagemaker_runtime.types.part_blob.PartBlob"]
    """<p>A blob that contains part of the response for your streaming inference request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PayloadPart) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PayloadPart:
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: PayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "PayloadPart"}
    payload = b""
    payload = value["bytes"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> PayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    if payload:
        out["bytes"] = payload
    return out
