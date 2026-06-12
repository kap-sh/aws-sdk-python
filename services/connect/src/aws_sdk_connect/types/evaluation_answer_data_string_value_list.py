"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswerDataStringValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_answer_data_string_value

EvaluationAnswerDataStringValueList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_answer_data_string_value.EvaluationAnswerDataStringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAnswerDataStringValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationAnswerDataStringValueList:
    return list(data)
