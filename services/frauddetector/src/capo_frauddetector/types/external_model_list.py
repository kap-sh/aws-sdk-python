"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.external_model

ExternalModelList: TypeAlias = list[
    "capo_frauddetector.types.external_model.ExternalModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalModelList) -> list:
    import capo_frauddetector.types.external_model

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.external_model.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExternalModelList:
    import capo_frauddetector.types.external_model

    out: ExternalModelList = []
    for item in data:
        out.append(
            capo_frauddetector.types.external_model.deserialize_aws_json_1_1(item)
        )
    return out
