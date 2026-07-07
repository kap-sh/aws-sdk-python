"""Generated from Smithy shape ``com.amazonaws.sqs#SendMessageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string


class SendMessageResult(TypedDict, closed=True):
    md5_of_message_body: NotRequired["aws_sdk_sqs.types.string.String"]
    r"""<p>An MD5 digest of the non-URL-encoded message body string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see <a href=\"https://www.ietf.org/rfc/rfc1321.txt\">RFC1321</a>.</p>"""
    md5_of_message_attributes: NotRequired["aws_sdk_sqs.types.string.String"]
    r"""<p>An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see <a href=\"https://www.ietf.org/rfc/rfc1321.txt\">RFC1321</a>.</p>"""
    md5_of_message_system_attributes: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>An MD5 digest of the non-URL-encoded message system attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest.</p>"""
    message_id: NotRequired["aws_sdk_sqs.types.string.String"]
    r"""<p>An attribute containing the <code>MessageId</code> of the message sent to the queue. For more information, see <a href=\"https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html\">Queue and Message Identifiers</a> in the <i>Amazon SQS Developer Guide</i>. </p>"""
    sequence_number: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>This parameter applies only to FIFO (first-in-first-out) queues.</p> <p>The large, non-consecutive number that Amazon SQS assigns to each message.</p> <p>The length of <code>SequenceNumber</code> is 128 bits. <code>SequenceNumber</code> continues to increase for a particular <code>MessageGroupId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendMessageResult) -> dict:
    out: dict = {}
    if "md5_of_message_body" in value:
        out["MD5OfMessageBody"] = value["md5_of_message_body"]
    if "md5_of_message_attributes" in value:
        out["MD5OfMessageAttributes"] = value["md5_of_message_attributes"]
    if "md5_of_message_system_attributes" in value:
        out["MD5OfMessageSystemAttributes"] = value["md5_of_message_system_attributes"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "sequence_number" in value:
        out["SequenceNumber"] = value["sequence_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendMessageResult:
    out: SendMessageResult = {}  # type: ignore[typeddict-item]
    if "MD5OfMessageBody" in data:
        out["md5_of_message_body"] = data["MD5OfMessageBody"]
    if "MD5OfMessageAttributes" in data:
        out["md5_of_message_attributes"] = data["MD5OfMessageAttributes"]
    if "MD5OfMessageSystemAttributes" in data:
        out["md5_of_message_system_attributes"] = data["MD5OfMessageSystemAttributes"]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "SequenceNumber" in data:
        out["sequence_number"] = data["SequenceNumber"]
    return out
