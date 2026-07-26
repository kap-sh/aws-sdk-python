"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfEvaluatedModelVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.evaluated_model_version

ListOfEvaluatedModelVersions: TypeAlias = list[
    "capo_frauddetector.types.evaluated_model_version.EvaluatedModelVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEvaluatedModelVersions) -> list:
    import capo_frauddetector.types.evaluated_model_version

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.evaluated_model_version.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEvaluatedModelVersions:
    import capo_frauddetector.types.evaluated_model_version

    out: ListOfEvaluatedModelVersions = []
    for item in data:
        out.append(
            capo_frauddetector.types.evaluated_model_version.deserialize_aws_json_1_1(
                item
            )
        )
    return out
