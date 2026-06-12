"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MatchedCategoryDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.points_of_interest
    import aws_sdk_transcribe_streaming.types.string

MatchedCategoryDetails: TypeAlias = dict[
    "aws_sdk_transcribe_streaming.types.string.String",
    "aws_sdk_transcribe_streaming.types.points_of_interest.PointsOfInterest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MatchedCategoryDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_transcribe_streaming.types.points_of_interest

        out[key] = aws_sdk_transcribe_streaming.types.points_of_interest.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> MatchedCategoryDetails:
    out: MatchedCategoryDetails = {}
    for key, value in data.items():
        import aws_sdk_transcribe_streaming.types.points_of_interest

        out[key] = (
            aws_sdk_transcribe_streaming.types.points_of_interest.deserialize_json(
                value
            )
        )
    return out
