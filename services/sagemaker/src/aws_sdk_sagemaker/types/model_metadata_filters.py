"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_metadata_filter

ModelMetadataFilters: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_metadata_filter.ModelMetadataFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetadataFilters) -> list:
    import aws_sdk_sagemaker.types.model_metadata_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_metadata_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelMetadataFilters:
    import aws_sdk_sagemaker.types.model_metadata_filter

    out: ModelMetadataFilters = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_metadata_filter.deserialize_aws_json_1_1(item)
        )
    return out
