"""Generated from Smithy shape ``com.amazonaws.apprunner#AutoScalingConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apprunner.types.auto_scaling_configuration_summary

AutoScalingConfigurationSummaryList: TypeAlias = list[
    "capo_apprunner.types.auto_scaling_configuration_summary.AutoScalingConfigurationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingConfigurationSummaryList) -> list:
    import capo_apprunner.types.auto_scaling_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_apprunner.types.auto_scaling_configuration_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutoScalingConfigurationSummaryList:
    import capo_apprunner.types.auto_scaling_configuration_summary

    out: AutoScalingConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_apprunner.types.auto_scaling_configuration_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
