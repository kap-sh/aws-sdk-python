"""Generated from Smithy shape ``com.amazonaws.connect#EmailAttachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.email_attachment

EmailAttachments: TypeAlias = list[
    "capo_connect.types.email_attachment.EmailAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAttachments) -> list:
    import capo_connect.types.email_attachment

    out: list = []
    for item in value:
        out.append(capo_connect.types.email_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAttachments:
    import capo_connect.types.email_attachment

    out: EmailAttachments = []
    for item in data:
        out.append(capo_connect.types.email_attachment.deserialize_json(item))
    return out
