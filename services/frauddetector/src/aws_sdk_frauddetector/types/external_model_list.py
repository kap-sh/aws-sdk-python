"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.external_model

ExternalModelList: TypeAlias = list[
    "aws_sdk_frauddetector.types.external_model.ExternalModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalModelList) -> list:
    import aws_sdk_frauddetector.types.external_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.external_model.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExternalModelList:
    import aws_sdk_frauddetector.types.external_model

    out: ExternalModelList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.external_model.deserialize_aws_json_1_1(item)
        )
    return out
