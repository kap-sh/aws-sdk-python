"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CustomArtifactsConfigurationDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.custom_artifact_configuration_description

CustomArtifactsConfigurationDescriptionList: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.custom_artifact_configuration_description.CustomArtifactConfigurationDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomArtifactsConfigurationDescriptionList) -> list:
    import aws_sdk_kinesis_analytics_v2.types.custom_artifact_configuration_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.custom_artifact_configuration_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomArtifactsConfigurationDescriptionList:
    import aws_sdk_kinesis_analytics_v2.types.custom_artifact_configuration_description

    out: CustomArtifactsConfigurationDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.custom_artifact_configuration_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
