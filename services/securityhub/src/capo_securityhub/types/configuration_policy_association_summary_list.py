"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicyAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.configuration_policy_association_summary

ConfigurationPolicyAssociationSummaryList: TypeAlias = list[
    "capo_securityhub.types.configuration_policy_association_summary.ConfigurationPolicyAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationPolicyAssociationSummaryList) -> list:
    import capo_securityhub.types.configuration_policy_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.configuration_policy_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationPolicyAssociationSummaryList:
    import capo_securityhub.types.configuration_policy_association_summary

    out: ConfigurationPolicyAssociationSummaryList = []
    for item in data:
        out.append(
            capo_securityhub.types.configuration_policy_association_summary.deserialize_json(
                item
            )
        )
    return out
