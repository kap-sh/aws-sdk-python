"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.configuration_recorder_summary

ConfigurationRecorderSummaries: TypeAlias = list[
    "capo_config_service.types.configuration_recorder_summary.ConfigurationRecorderSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderSummaries) -> list:
    import capo_config_service.types.configuration_recorder_summary

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.configuration_recorder_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationRecorderSummaries:
    import capo_config_service.types.configuration_recorder_summary

    out: ConfigurationRecorderSummaries = []
    for item in data:
        out.append(
            capo_config_service.types.configuration_recorder_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
