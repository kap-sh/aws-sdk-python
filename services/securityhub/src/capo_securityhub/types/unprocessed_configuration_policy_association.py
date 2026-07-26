"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedConfigurationPolicyAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.configuration_policy_association
    import capo_securityhub.types.non_empty_string


class UnprocessedConfigurationPolicyAssociation(TypedDict, closed=True):
    configuration_policy_association_identifiers: NotRequired[
        "capo_securityhub.types.configuration_policy_association.ConfigurationPolicyAssociation"
    ]
    """<p> Configuration policy association identifiers that were specified in a <code>BatchGetConfigurationPolicyAssociations</code> request but couldn’t be processed due to an error. </p>"""
    error_code: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> An HTTP status code that identifies why the configuration policy association failed. </p>"""
    error_reason: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> A string that identifies why the configuration policy association failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedConfigurationPolicyAssociation) -> dict:
    out: dict = {}
    if "configuration_policy_association_identifiers" in value:
        import capo_securityhub.types.configuration_policy_association

        out["ConfigurationPolicyAssociationIdentifiers"] = (
            capo_securityhub.types.configuration_policy_association.serialize_json(
                value["configuration_policy_association_identifiers"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_reason" in value:
        out["ErrorReason"] = value["error_reason"]
    return out


def deserialize_json(data: dict) -> UnprocessedConfigurationPolicyAssociation:
    out: UnprocessedConfigurationPolicyAssociation = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicyAssociationIdentifiers" in data:
        import capo_securityhub.types.configuration_policy_association

        out["configuration_policy_association_identifiers"] = (
            capo_securityhub.types.configuration_policy_association.deserialize_json(
                data["ConfigurationPolicyAssociationIdentifiers"]
            )
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorReason" in data:
        out["error_reason"] = data["ErrorReason"]
    return out
