"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfModelVersionEvaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.model_version_evaluation

ListOfModelVersionEvaluations: TypeAlias = list[
    "capo_frauddetector.types.model_version_evaluation.ModelVersionEvaluation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfModelVersionEvaluations) -> list:
    import capo_frauddetector.types.model_version_evaluation

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.model_version_evaluation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfModelVersionEvaluations:
    import capo_frauddetector.types.model_version_evaluation

    out: ListOfModelVersionEvaluations = []
    for item in data:
        out.append(
            capo_frauddetector.types.model_version_evaluation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
