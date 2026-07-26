"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicyAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.configuration_policy_association_summary

ConfigurationPolicyAssociationList: TypeAlias = list[
    "capo_securityhub.types.configuration_policy_association_summary.ConfigurationPolicyAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationPolicyAssociationList) -> list:
    import capo_securityhub.types.configuration_policy_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.configuration_policy_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationPolicyAssociationList:
    import capo_securityhub.types.configuration_policy_association_summary

    out: ConfigurationPolicyAssociationList = []
    for item in data:
        out.append(
            capo_securityhub.types.configuration_policy_association_summary.deserialize_json(
                item
            )
        )
    return out
