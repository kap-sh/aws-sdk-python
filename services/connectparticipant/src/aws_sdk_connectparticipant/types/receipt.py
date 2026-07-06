"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Receipt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.instant
    import aws_sdk_connectparticipant.types.participant_id


class Receipt(TypedDict, closed=True):
    delivered_timestamp: NotRequired["aws_sdk_connectparticipant.types.instant.Instant"]
    """<p>The time when the message was delivered to the recipient.</p>"""
    read_timestamp: NotRequired["aws_sdk_connectparticipant.types.instant.Instant"]
    """<p>The time when the message was read by the recipient.</p>"""
    recipient_participant_id: NotRequired[
        "aws_sdk_connectparticipant.types.participant_id.ParticipantId"
    ]
    """<p>The identifier of the recipient of the message. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Receipt) -> dict:
    out: dict = {}
    if "delivered_timestamp" in value:
        out["DeliveredTimestamp"] = value["delivered_timestamp"]
    if "read_timestamp" in value:
        out["ReadTimestamp"] = value["read_timestamp"]
    if "recipient_participant_id" in value:
        out["RecipientParticipantId"] = value["recipient_participant_id"]
    return out


def deserialize_json(data: dict) -> Receipt:
    out: Receipt = {}  # type: ignore[typeddict-item]
    if "DeliveredTimestamp" in data:
        out["delivered_timestamp"] = data["DeliveredTimestamp"]
    if "ReadTimestamp" in data:
        out["read_timestamp"] = data["ReadTimestamp"]
    if "RecipientParticipantId" in data:
        out["recipient_participant_id"] = data["RecipientParticipantId"]
    return out
