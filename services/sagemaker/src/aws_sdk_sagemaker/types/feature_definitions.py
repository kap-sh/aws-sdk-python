"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_definition

FeatureDefinitions: TypeAlias = list[
    "aws_sdk_sagemaker.types.feature_definition.FeatureDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureDefinitions) -> list:
    import aws_sdk_sagemaker.types.feature_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.feature_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeatureDefinitions:
    import aws_sdk_sagemaker.types.feature_definition

    out: FeatureDefinitions = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.feature_definition.deserialize_aws_json_1_1(item)
        )
    return out
