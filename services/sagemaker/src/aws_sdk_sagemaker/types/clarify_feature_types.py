"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyFeatureTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.clarify_feature_type

ClarifyFeatureTypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.clarify_feature_type.ClarifyFeatureType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyFeatureTypes) -> list:
    import aws_sdk_sagemaker.types.clarify_feature_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.clarify_feature_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClarifyFeatureTypes:
    import aws_sdk_sagemaker.types.clarify_feature_type

    out: ClarifyFeatureTypes = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.clarify_feature_type.deserialize_aws_json_1_1(item)
        )
    return out
