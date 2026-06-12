"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchResultEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.message_id
    import aws_sdk_sns.types.string


class PublishBatchResultEntry(TypedDict):
    id: NotRequired["aws_sdk_sns.types.string.String"]
    """<p>The <code>Id</code> of an entry in a batch request.</p>"""
    message_id: NotRequired["aws_sdk_sns.types.message_id.messageId"]
    """<p>An identifier for the message.</p>"""
    sequence_number: NotRequired["aws_sdk_sns.types.string.String"]
    """<p>This parameter applies only to FIFO (first-in-first-out) topics.</p> <p>The large, non-consecutive number that Amazon SNS assigns to each message.</p> <p>The length of <code>SequenceNumber</code> is 128 bits. <code>SequenceNumber</code> continues to increase for a particular <code>MessageGroupId</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchResultEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "message_id" in value:
        pairs.append((f"{prefix}.MessageId", str(value["message_id"])))
    if "sequence_number" in value:
        pairs.append((f"{prefix}.SequenceNumber", str(value["sequence_number"])))


def deserialize_query(el: Element) -> PublishBatchResultEntry:
    out: PublishBatchResultEntry = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_message_id = el.find("MessageId")
    if child_message_id is not None:
        out["message_id"] = str(child_message_id.text or "")
    child_sequence_number = el.find("SequenceNumber")
    if child_sequence_number is not None:
        out["sequence_number"] = str(child_sequence_number.text or "")
    return out
