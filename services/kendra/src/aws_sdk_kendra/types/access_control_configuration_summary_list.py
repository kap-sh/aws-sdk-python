"""Generated from Smithy shape ``com.amazonaws.kendra#AccessControlConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.access_control_configuration_summary

AccessControlConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_kendra.types.access_control_configuration_summary.AccessControlConfigurationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlConfigurationSummaryList) -> list:
    import aws_sdk_kendra.types.access_control_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.access_control_configuration_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccessControlConfigurationSummaryList:
    import aws_sdk_kendra.types.access_control_configuration_summary

    out: AccessControlConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.access_control_configuration_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
