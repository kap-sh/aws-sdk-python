"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationTranscriptPointsOfInterest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_transcript_point_of_interest

EvaluationTranscriptPointsOfInterest: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_transcript_point_of_interest.EvaluationTranscriptPointOfInterest"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationTranscriptPointsOfInterest) -> list:
    import aws_sdk_connect.types.evaluation_transcript_point_of_interest

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_transcript_point_of_interest.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationTranscriptPointsOfInterest:
    import aws_sdk_connect.types.evaluation_transcript_point_of_interest

    out: EvaluationTranscriptPointsOfInterest = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_transcript_point_of_interest.deserialize_json(
                item
            )
        )
    return out
