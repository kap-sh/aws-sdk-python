"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#SequenceNumberRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.sequence_number


class SequenceNumberRange(TypedDict):
    starting_sequence_number: NotRequired[
        "aws_sdk_keyspacesstreams.types.sequence_number.SequenceNumber"
    ]
    """<p>The starting sequence number of the range.</p>"""
    ending_sequence_number: NotRequired[
        "aws_sdk_keyspacesstreams.types.sequence_number.SequenceNumber"
    ]
    """<p>The ending sequence number of the range, which may be null for open-ended ranges.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SequenceNumberRange) -> dict:
    out: dict = {}
    if "starting_sequence_number" in value:
        out["startingSequenceNumber"] = value["starting_sequence_number"]
    if "ending_sequence_number" in value:
        out["endingSequenceNumber"] = value["ending_sequence_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SequenceNumberRange:
    out: SequenceNumberRange = {}  # type: ignore[typeddict-item]
    if "startingSequenceNumber" in data:
        out["starting_sequence_number"] = data["startingSequenceNumber"]
    if "endingSequenceNumber" in data:
        out["ending_sequence_number"] = data["endingSequenceNumber"]
    return out
