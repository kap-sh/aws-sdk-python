"""Generated from Smithy shape ``com.amazonaws.apprunner#ObservabilityConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.observability_configuration_summary

ObservabilityConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_apprunner.types.observability_configuration_summary.ObservabilityConfigurationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ObservabilityConfigurationSummaryList) -> list:
    import aws_sdk_apprunner.types.observability_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_apprunner.types.observability_configuration_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ObservabilityConfigurationSummaryList:
    import aws_sdk_apprunner.types.observability_configuration_summary

    out: ObservabilityConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_apprunner.types.observability_configuration_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
