"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicyAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.configuration_policy_association

ConfigurationPolicyAssociationsList: TypeAlias = list[
    "capo_securityhub.types.configuration_policy_association.ConfigurationPolicyAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationPolicyAssociationsList) -> list:
    import capo_securityhub.types.configuration_policy_association

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.configuration_policy_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationPolicyAssociationsList:
    import capo_securityhub.types.configuration_policy_association

    out: ConfigurationPolicyAssociationsList = []
    for item in data:
        out.append(
            capo_securityhub.types.configuration_policy_association.deserialize_json(
                item
            )
        )
    return out
