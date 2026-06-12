"""Generated from Smithy shape ``com.amazonaws.frauddetector#modelVersionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.model_version_detail

modelVersionDetailList: TypeAlias = list[
    "aws_sdk_frauddetector.types.model_version_detail.ModelVersionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: modelVersionDetailList) -> list:
    import aws_sdk_frauddetector.types.model_version_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.model_version_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> modelVersionDetailList:
    import aws_sdk_frauddetector.types.model_version_detail

    out: modelVersionDetailList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.model_version_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
