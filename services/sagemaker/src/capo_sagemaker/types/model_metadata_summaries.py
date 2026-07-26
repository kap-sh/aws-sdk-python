"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.model_metadata_summary

ModelMetadataSummaries: TypeAlias = list[
    "capo_sagemaker.types.model_metadata_summary.ModelMetadataSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetadataSummaries) -> list:
    import capo_sagemaker.types.model_metadata_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.model_metadata_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelMetadataSummaries:
    import capo_sagemaker.types.model_metadata_summary

    out: ModelMetadataSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.model_metadata_summary.deserialize_aws_json_1_1(item)
        )
    return out
