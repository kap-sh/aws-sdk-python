"""Generated from Smithy shape ``com.amazonaws.connect#EmailAttachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_attachment

EmailAttachments: TypeAlias = list[
    "aws_sdk_connect.types.email_attachment.EmailAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAttachments) -> list:
    import aws_sdk_connect.types.email_attachment

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.email_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAttachments:
    import aws_sdk_connect.types.email_attachment

    out: EmailAttachments = []
    for item in data:
        out.append(aws_sdk_connect.types.email_attachment.deserialize_json(item))
    return out
