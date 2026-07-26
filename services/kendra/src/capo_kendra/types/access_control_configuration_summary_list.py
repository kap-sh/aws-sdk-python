"""Generated from Smithy shape ``com.amazonaws.kendra#AccessControlConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_summary

AccessControlConfigurationSummaryList: TypeAlias = list[
    "capo_kendra.types.access_control_configuration_summary.AccessControlConfigurationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlConfigurationSummaryList) -> list:
    import capo_kendra.types.access_control_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.access_control_configuration_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccessControlConfigurationSummaryList:
    import capo_kendra.types.access_control_configuration_summary

    out: AccessControlConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_kendra.types.access_control_configuration_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
