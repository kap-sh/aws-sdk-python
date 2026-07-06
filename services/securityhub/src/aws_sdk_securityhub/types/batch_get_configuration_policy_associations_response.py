"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetConfigurationPolicyAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.configuration_policy_association_list
    import aws_sdk_securityhub.types.unprocessed_configuration_policy_association_list


class BatchGetConfigurationPolicyAssociationsResponse(TypedDict, closed=True):
    configuration_policy_associations: NotRequired[
        "aws_sdk_securityhub.types.configuration_policy_association_list.ConfigurationPolicyAssociationList"
    ]
    """<p> Describes associations for the target accounts, OUs, or the root. </p>"""
    unprocessed_configuration_policy_associations: NotRequired[
        "aws_sdk_securityhub.types.unprocessed_configuration_policy_association_list.UnprocessedConfigurationPolicyAssociationList"
    ]
    """<p> An array of configuration policy associations, one for each configuration policy association identifier, that was specified in the request but couldn’t be processed due to an error. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetConfigurationPolicyAssociationsResponse) -> dict:
    out: dict = {}
    if "configuration_policy_associations" in value:
        import aws_sdk_securityhub.types.configuration_policy_association_list

        out["ConfigurationPolicyAssociations"] = (
            aws_sdk_securityhub.types.configuration_policy_association_list.serialize_json(
                value["configuration_policy_associations"]
            )
        )
    if "unprocessed_configuration_policy_associations" in value:
        import aws_sdk_securityhub.types.unprocessed_configuration_policy_association_list

        out["UnprocessedConfigurationPolicyAssociations"] = (
            aws_sdk_securityhub.types.unprocessed_configuration_policy_association_list.serialize_json(
                value["unprocessed_configuration_policy_associations"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetConfigurationPolicyAssociationsResponse:
    out: BatchGetConfigurationPolicyAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicyAssociations" in data:
        import aws_sdk_securityhub.types.configuration_policy_association_list

        out["configuration_policy_associations"] = (
            aws_sdk_securityhub.types.configuration_policy_association_list.deserialize_json(
                data["ConfigurationPolicyAssociations"]
            )
        )
    if "UnprocessedConfigurationPolicyAssociations" in data:
        import aws_sdk_securityhub.types.unprocessed_configuration_policy_association_list

        out["unprocessed_configuration_policy_associations"] = (
            aws_sdk_securityhub.types.unprocessed_configuration_policy_association_list.deserialize_json(
                data["UnprocessedConfigurationPolicyAssociations"]
            )
        )
    return out
