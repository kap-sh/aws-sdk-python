"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalModelDataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_model_data_source

AdditionalModelDataSources: TypeAlias = list[
    "aws_sdk_sagemaker.types.additional_model_data_source.AdditionalModelDataSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalModelDataSources) -> list:
    import aws_sdk_sagemaker.types.additional_model_data_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.additional_model_data_source.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdditionalModelDataSources:
    import aws_sdk_sagemaker.types.additional_model_data_source

    out: AdditionalModelDataSources = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.additional_model_data_source.deserialize_aws_json_1_1(
                item
            )
        )
    return out
