"""Generated from Smithy shape ``com.amazonaws.sagemaker#HiddenSageMakerImageVersionAliasesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hidden_sage_maker_image

HiddenSageMakerImageVersionAliasesList: TypeAlias = list[
    "capo_sagemaker.types.hidden_sage_maker_image.HiddenSageMakerImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HiddenSageMakerImageVersionAliasesList) -> list:
    import capo_sagemaker.types.hidden_sage_maker_image

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.hidden_sage_maker_image.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HiddenSageMakerImageVersionAliasesList:
    import capo_sagemaker.types.hidden_sage_maker_image

    out: HiddenSageMakerImageVersionAliasesList = []
    for item in data:
        out.append(
            capo_sagemaker.types.hidden_sage_maker_image.deserialize_aws_json_1_1(item)
        )
    return out
