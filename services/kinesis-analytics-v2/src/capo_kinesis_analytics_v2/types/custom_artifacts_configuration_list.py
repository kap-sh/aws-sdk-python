"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CustomArtifactsConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.custom_artifact_configuration

CustomArtifactsConfigurationList: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.custom_artifact_configuration.CustomArtifactConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomArtifactsConfigurationList) -> list:
    import capo_kinesis_analytics_v2.types.custom_artifact_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.custom_artifact_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomArtifactsConfigurationList:
    import capo_kinesis_analytics_v2.types.custom_artifact_configuration

    out: CustomArtifactsConfigurationList = []
    for item in data:
        out.append(
            capo_kinesis_analytics_v2.types.custom_artifact_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
