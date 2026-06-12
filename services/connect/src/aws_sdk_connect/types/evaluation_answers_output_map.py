"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswersOutputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_answer_output
    import aws_sdk_connect.types.resource_id

EvaluationAnswersOutputMap: TypeAlias = dict[
    "aws_sdk_connect.types.resource_id.ResourceId",
    "aws_sdk_connect.types.evaluation_answer_output.EvaluationAnswerOutput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EvaluationAnswersOutputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.evaluation_answer_output

        out[key] = aws_sdk_connect.types.evaluation_answer_output.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EvaluationAnswersOutputMap:
    out: EvaluationAnswersOutputMap = {}
    for key, value in data.items():
        import aws_sdk_connect.types.evaluation_answer_output

        out[key] = aws_sdk_connect.types.evaluation_answer_output.deserialize_json(
            value
        )
    return out
