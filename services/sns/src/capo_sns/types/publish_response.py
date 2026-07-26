"""Generated from Smithy shape ``com.amazonaws.sns#PublishResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.message_id
    import capo_sns.types.string


class PublishResponse(TypedDict, closed=True):
    message_id: NotRequired["capo_sns.types.message_id.messageId"]
    """<p>Unique identifier assigned to the published message.</p> <p>Length Constraint: Maximum 100 characters</p>"""
    sequence_number: NotRequired["capo_sns.types.string.String"]
    """<p>This response element applies only to FIFO (first-in-first-out) topics. </p> <p>The sequence number is a large, non-consecutive number that Amazon SNS assigns to each message. The length of <code>SequenceNumber</code> is 128 bits. <code>SequenceNumber</code> continues to increase for each <code>MessageGroupId</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message_id" in value:
        pairs.append((f"{prefix}.MessageId", str(value["message_id"])))
    if "sequence_number" in value:
        pairs.append((f"{prefix}.SequenceNumber", str(value["sequence_number"])))


def deserialize_query(el: Element) -> PublishResponse:
    out: PublishResponse = {}  # type: ignore[typeddict-item]
    child_message_id = el.find("MessageId")
    if child_message_id is not None:
        out["message_id"] = str(child_message_id.text or "")
    child_sequence_number = el.find("SequenceNumber")
    if child_sequence_number is not None:
        out["sequence_number"] = str(child_sequence_number.text or "")
    return out
