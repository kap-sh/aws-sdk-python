"""Generated from Smithy shape ``com.amazonaws.connect#EmailRecipientsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_recipient

EmailRecipientsList: TypeAlias = list[
    "aws_sdk_connect.types.email_recipient.EmailRecipient"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailRecipientsList) -> list:
    import aws_sdk_connect.types.email_recipient

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.email_recipient.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailRecipientsList:
    import aws_sdk_connect.types.email_recipient

    out: EmailRecipientsList = []
    for item in data:
        out.append(aws_sdk_connect.types.email_recipient.deserialize_json(item))
    return out
