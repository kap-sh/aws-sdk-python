"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentInputEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_input


class AttachmentInputEvent(TypedDict, closed=True):
    attachment: NotRequired["capo_qbusiness.types.attachment_input.AttachmentInput"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentInputEvent) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_qbusiness.types.attachment_input

        out["attachment"] = capo_qbusiness.types.attachment_input.serialize_json(
            value["attachment"]
        )
    return out


def deserialize_json(data: dict) -> AttachmentInputEvent:
    out: AttachmentInputEvent = {}  # type: ignore[typeddict-item]
    if "attachment" in data:
        import capo_qbusiness.types.attachment_input

        out["attachment"] = capo_qbusiness.types.attachment_input.deserialize_json(
            data["attachment"]
        )
    return out


def serialize_event_json(value: AttachmentInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "attachmentEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AttachmentInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AttachmentInputEvent = {}  # type: ignore[typeddict-item]
    return out
