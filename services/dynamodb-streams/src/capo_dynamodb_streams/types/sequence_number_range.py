"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#SequenceNumberRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.sequence_number


class SequenceNumberRange(TypedDict, closed=True):
    starting_sequence_number: NotRequired[
        "capo_dynamodb_streams.types.sequence_number.SequenceNumber"
    ]
    """<p>The first sequence number for the stream records contained within a shard. String contains numeric characters only.</p>"""
    ending_sequence_number: NotRequired[
        "capo_dynamodb_streams.types.sequence_number.SequenceNumber"
    ]
    """<p>The last sequence number for the stream records contained within a shard. String contains numeric characters only.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SequenceNumberRange) -> dict:
    out: dict = {}
    if "starting_sequence_number" in value:
        out["StartingSequenceNumber"] = value["starting_sequence_number"]
    if "ending_sequence_number" in value:
        out["EndingSequenceNumber"] = value["ending_sequence_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SequenceNumberRange:
    out: SequenceNumberRange = {}  # type: ignore[typeddict-item]
    if "StartingSequenceNumber" in data:
        out["starting_sequence_number"] = data["StartingSequenceNumber"]
    if "EndingSequenceNumber" in data:
        out["ending_sequence_number"] = data["EndingSequenceNumber"]
    return out
