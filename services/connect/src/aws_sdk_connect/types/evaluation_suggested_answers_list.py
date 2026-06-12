"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSuggestedAnswersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_suggested_answer

EvaluationSuggestedAnswersList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_suggested_answer.EvaluationSuggestedAnswer"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSuggestedAnswersList) -> list:
    import aws_sdk_connect.types.evaluation_suggested_answer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_suggested_answer.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationSuggestedAnswersList:
    import aws_sdk_connect.types.evaluation_suggested_answer

    out: EvaluationSuggestedAnswersList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_suggested_answer.deserialize_json(item)
        )
    return out
