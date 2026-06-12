"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.configuration_policy_summary

ConfigurationPolicySummaryList: TypeAlias = list[
    "aws_sdk_securityhub.types.configuration_policy_summary.ConfigurationPolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationPolicySummaryList) -> list:
    import aws_sdk_securityhub.types.configuration_policy_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.configuration_policy_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationPolicySummaryList:
    import aws_sdk_securityhub.types.configuration_policy_summary

    out: ConfigurationPolicySummaryList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.configuration_policy_summary.deserialize_json(
                item
            )
        )
    return out
