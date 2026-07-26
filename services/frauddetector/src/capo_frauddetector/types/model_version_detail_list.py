"""Generated from Smithy shape ``com.amazonaws.frauddetector#modelVersionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.model_version_detail

modelVersionDetailList: TypeAlias = list[
    "capo_frauddetector.types.model_version_detail.ModelVersionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: modelVersionDetailList) -> list:
    import capo_frauddetector.types.model_version_detail

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.model_version_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> modelVersionDetailList:
    import capo_frauddetector.types.model_version_detail

    out: modelVersionDetailList = []
    for item in data:
        out.append(
            capo_frauddetector.types.model_version_detail.deserialize_aws_json_1_1(item)
        )
    return out
