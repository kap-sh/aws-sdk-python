"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetConfigurationPolicyAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.configuration_policy_associations_list


class BatchGetConfigurationPolicyAssociationsRequest(TypedDict):
    configuration_policy_association_identifiers: NotRequired[
        "aws_sdk_securityhub.types.configuration_policy_associations_list.ConfigurationPolicyAssociationsList"
    ]
    """<p> Specifies one or more target account IDs, organizational unit (OU) IDs, or the root ID to retrieve associations for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetConfigurationPolicyAssociationsRequest) -> dict:
    out: dict = {}
    if "configuration_policy_association_identifiers" in value:
        import aws_sdk_securityhub.types.configuration_policy_associations_list

        out["ConfigurationPolicyAssociationIdentifiers"] = (
            aws_sdk_securityhub.types.configuration_policy_associations_list.serialize_json(
                value["configuration_policy_association_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetConfigurationPolicyAssociationsRequest:
    out: BatchGetConfigurationPolicyAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicyAssociationIdentifiers" in data:
        import aws_sdk_securityhub.types.configuration_policy_associations_list

        out["configuration_policy_association_identifiers"] = (
            aws_sdk_securityhub.types.configuration_policy_associations_list.deserialize_json(
                data["ConfigurationPolicyAssociationIdentifiers"]
            )
        )
    return out
