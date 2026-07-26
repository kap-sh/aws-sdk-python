"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_definition

FeatureDefinitions: TypeAlias = list[
    "capo_sagemaker.types.feature_definition.FeatureDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureDefinitions) -> list:
    import capo_sagemaker.types.feature_definition

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.feature_definition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FeatureDefinitions:
    import capo_sagemaker.types.feature_definition

    out: FeatureDefinitions = []
    for item in data:
        out.append(
            capo_sagemaker.types.feature_definition.deserialize_aws_json_1_1(item)
        )
    return out
