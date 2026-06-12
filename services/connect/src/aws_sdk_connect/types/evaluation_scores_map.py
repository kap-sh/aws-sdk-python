"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationScoresMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_score
    import aws_sdk_connect.types.resource_id

EvaluationScoresMap: TypeAlias = dict[
    "aws_sdk_connect.types.resource_id.ResourceId",
    "aws_sdk_connect.types.evaluation_score.EvaluationScore",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EvaluationScoresMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.evaluation_score

        out[key] = aws_sdk_connect.types.evaluation_score.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EvaluationScoresMap:
    out: EvaluationScoresMap = {}
    for key, value in data.items():
        import aws_sdk_connect.types.evaluation_score

        out[key] = aws_sdk_connect.types.evaluation_score.deserialize_json(value)
    return out
