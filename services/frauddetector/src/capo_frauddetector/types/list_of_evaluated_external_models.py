"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfEvaluatedExternalModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.evaluated_external_model

ListOfEvaluatedExternalModels: TypeAlias = list[
    "capo_frauddetector.types.evaluated_external_model.EvaluatedExternalModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEvaluatedExternalModels) -> list:
    import capo_frauddetector.types.evaluated_external_model

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.evaluated_external_model.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEvaluatedExternalModels:
    import capo_frauddetector.types.evaluated_external_model

    out: ListOfEvaluatedExternalModels = []
    for item in data:
        out.append(
            capo_frauddetector.types.evaluated_external_model.deserialize_aws_json_1_1(
                item
            )
        )
    return out
