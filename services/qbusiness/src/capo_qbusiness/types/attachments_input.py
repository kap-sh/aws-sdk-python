"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentsInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_input

AttachmentsInput: TypeAlias = list[
    "capo_qbusiness.types.attachment_input.AttachmentInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentsInput) -> list:
    import capo_qbusiness.types.attachment_input

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.attachment_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachmentsInput:
    import capo_qbusiness.types.attachment_input

    out: AttachmentsInput = []
    for item in data:
        out.append(capo_qbusiness.types.attachment_input.deserialize_json(item))
    return out
