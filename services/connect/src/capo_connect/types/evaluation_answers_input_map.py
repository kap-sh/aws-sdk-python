"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswersInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_answer_input
    import capo_connect.types.resource_id

EvaluationAnswersInputMap: TypeAlias = dict[
    "capo_connect.types.resource_id.ResourceId",
    "capo_connect.types.evaluation_answer_input.EvaluationAnswerInput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EvaluationAnswersInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.evaluation_answer_input

        out[key] = capo_connect.types.evaluation_answer_input.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EvaluationAnswersInputMap:
    out: EvaluationAnswersInputMap = {}
    for key, value in data.items():
        import capo_connect.types.evaluation_answer_input

        out[key] = capo_connect.types.evaluation_answer_input.deserialize_json(value)
    return out
