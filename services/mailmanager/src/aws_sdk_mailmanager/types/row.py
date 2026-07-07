"""Generated from Smithy shape ``com.amazonaws.mailmanager#Row``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.archived_message_id
    import aws_sdk_mailmanager.types.email_received_headers_list
    import aws_sdk_mailmanager.types.envelope
    import aws_sdk_mailmanager.types.ingress_point_id
    import aws_sdk_mailmanager.types.sender_ip_address

Row = TypedDict(
    "Row",
    {
        "archived_message_id": NotRequired[
            "aws_sdk_mailmanager.types.archived_message_id.ArchivedMessageId"
        ],
        "received_timestamp": NotRequired["datetime.datetime"],
        "date": NotRequired["str"],
        "to": NotRequired["str"],
        "from": NotRequired["str"],
        "cc": NotRequired["str"],
        "subject": NotRequired["str"],
        "message_id": NotRequired["str"],
        "has_attachments": NotRequired["bool"],
        "received_headers": NotRequired[
            "aws_sdk_mailmanager.types.email_received_headers_list.EmailReceivedHeadersList"
        ],
        "in_reply_to": NotRequired["str"],
        "x_mailer": NotRequired["str"],
        "x_original_mailer": NotRequired["str"],
        "x_priority": NotRequired["str"],
        "ingress_point_id": NotRequired[
            "aws_sdk_mailmanager.types.ingress_point_id.IngressPointId"
        ],
        "sender_hostname": NotRequired["str"],
        "sender_ip_address": NotRequired[
            "aws_sdk_mailmanager.types.sender_ip_address.SenderIpAddress"
        ],
        "envelope": NotRequired["aws_sdk_mailmanager.types.envelope.Envelope"],
        "source_arn": NotRequired["str"],
    },
    closed=True,
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Row) -> dict:
    out: dict = {}
    if "archived_message_id" in value:
        out["ArchivedMessageId"] = value["archived_message_id"]
    if "received_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["ReceivedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["received_timestamp"]
            )
        )
    if "date" in value:
        out["Date"] = value["date"]
    if "to" in value:
        out["To"] = value["to"]
    if "from" in value:
        out["From"] = value["from"]
    if "cc" in value:
        out["Cc"] = value["cc"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "has_attachments" in value:
        out["HasAttachments"] = value["has_attachments"]
    if "received_headers" in value:
        import aws_sdk_mailmanager.types.email_received_headers_list

        out["ReceivedHeaders"] = (
            aws_sdk_mailmanager.types.email_received_headers_list.serialize_aws_json_1_0(
                value["received_headers"]
            )
        )
    if "in_reply_to" in value:
        out["InReplyTo"] = value["in_reply_to"]
    if "x_mailer" in value:
        out["XMailer"] = value["x_mailer"]
    if "x_original_mailer" in value:
        out["XOriginalMailer"] = value["x_original_mailer"]
    if "x_priority" in value:
        out["XPriority"] = value["x_priority"]
    if "ingress_point_id" in value:
        out["IngressPointId"] = value["ingress_point_id"]
    if "sender_hostname" in value:
        out["SenderHostname"] = value["sender_hostname"]
    if "sender_ip_address" in value:
        out["SenderIpAddress"] = value["sender_ip_address"]
    if "envelope" in value:
        import aws_sdk_mailmanager.types.envelope

        out["Envelope"] = aws_sdk_mailmanager.types.envelope.serialize_aws_json_1_0(
            value["envelope"]
        )
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Row:
    out: Row = {}  # type: ignore[typeddict-item]
    if "ArchivedMessageId" in data:
        out["archived_message_id"] = data["ArchivedMessageId"]
    if "ReceivedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["received_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ReceivedTimestamp"]
            )
        )
    if "Date" in data:
        out["date"] = data["Date"]
    if "To" in data:
        out["to"] = data["To"]
    if "From" in data:
        out["from"] = data["From"]
    if "Cc" in data:
        out["cc"] = data["Cc"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "HasAttachments" in data:
        out["has_attachments"] = data["HasAttachments"]
    if "ReceivedHeaders" in data:
        import aws_sdk_mailmanager.types.email_received_headers_list

        out["received_headers"] = (
            aws_sdk_mailmanager.types.email_received_headers_list.deserialize_aws_json_1_0(
                data["ReceivedHeaders"]
            )
        )
    if "InReplyTo" in data:
        out["in_reply_to"] = data["InReplyTo"]
    if "XMailer" in data:
        out["x_mailer"] = data["XMailer"]
    if "XOriginalMailer" in data:
        out["x_original_mailer"] = data["XOriginalMailer"]
    if "XPriority" in data:
        out["x_priority"] = data["XPriority"]
    if "IngressPointId" in data:
        out["ingress_point_id"] = data["IngressPointId"]
    if "SenderHostname" in data:
        out["sender_hostname"] = data["SenderHostname"]
    if "SenderIpAddress" in data:
        out["sender_ip_address"] = data["SenderIpAddress"]
    if "Envelope" in data:
        import aws_sdk_mailmanager.types.envelope

        out["envelope"] = aws_sdk_mailmanager.types.envelope.deserialize_aws_json_1_0(
            data["Envelope"]
        )
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    return out
