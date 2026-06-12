"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedConfigurationPolicyAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.unprocessed_configuration_policy_association

UnprocessedConfigurationPolicyAssociationList: TypeAlias = list[
    "aws_sdk_securityhub.types.unprocessed_configuration_policy_association.UnprocessedConfigurationPolicyAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedConfigurationPolicyAssociationList) -> list:
    import aws_sdk_securityhub.types.unprocessed_configuration_policy_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.unprocessed_configuration_policy_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UnprocessedConfigurationPolicyAssociationList:
    import aws_sdk_securityhub.types.unprocessed_configuration_policy_association

    out: UnprocessedConfigurationPolicyAssociationList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.unprocessed_configuration_policy_association.deserialize_json(
                item
            )
        )
    return out
