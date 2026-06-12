"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_evaluation
    import aws_sdk_connect.types.evaluation_id

ContactEvaluations: TypeAlias = dict[
    "aws_sdk_connect.types.evaluation_id.EvaluationId",
    "aws_sdk_connect.types.contact_evaluation.ContactEvaluation",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ContactEvaluations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.contact_evaluation

        out[key] = aws_sdk_connect.types.contact_evaluation.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ContactEvaluations:
    out: ContactEvaluations = {}
    for key, value in data.items():
        import aws_sdk_connect.types.contact_evaluation

        out[key] = aws_sdk_connect.types.contact_evaluation.deserialize_json(value)
    return out
