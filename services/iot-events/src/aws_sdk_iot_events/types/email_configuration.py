"""Generated from Smithy shape ``com.amazonaws.iotevents#EmailConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.email_content
    import aws_sdk_iot_events.types.email_recipients
    import aws_sdk_iot_events.types.from_email

EmailConfiguration = TypedDict(
    "EmailConfiguration",
    {
        "from": "aws_sdk_iot_events.types.from_email.FromEmail",
        "content": NotRequired["aws_sdk_iot_events.types.email_content.EmailContent"],
        "recipients": "aws_sdk_iot_events.types.email_recipients.EmailRecipients",
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: EmailConfiguration) -> dict:
    out: dict = {}
    out["from"] = value["from"]
    if "content" in value:
        import aws_sdk_iot_events.types.email_content

        out["content"] = aws_sdk_iot_events.types.email_content.serialize_json(
            value["content"]
        )
    import aws_sdk_iot_events.types.email_recipients

    out["recipients"] = aws_sdk_iot_events.types.email_recipients.serialize_json(
        value["recipients"]
    )
    return out


def deserialize_json(data: dict) -> EmailConfiguration:
    out: EmailConfiguration = {}  # type: ignore[typeddict-item]
    if "from" in data:
        out["from"] = data["from"]
    else:
        raise DeserializationError("EmailConfiguration.from required")
    if "content" in data:
        import aws_sdk_iot_events.types.email_content

        out["content"] = aws_sdk_iot_events.types.email_content.deserialize_json(
            data["content"]
        )
    if "recipients" in data:
        import aws_sdk_iot_events.types.email_recipients

        out["recipients"] = aws_sdk_iot_events.types.email_recipients.deserialize_json(
            data["recipients"]
        )
    else:
        raise DeserializationError("EmailConfiguration.recipients required")
    return out
