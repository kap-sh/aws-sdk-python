"""Generated from Smithy shape ``com.amazonaws.securityhub#GetConfigurationPolicyAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.association_type
    import aws_sdk_securityhub.types.configuration_policy_association_status
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.target_type
    import aws_sdk_securityhub.types.timestamp


class GetConfigurationPolicyAssociationResponse(TypedDict):
    configuration_policy_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The universally unique identifier (UUID) of a configuration policy. For self-managed behavior, the value is <code>SELF_MANAGED_SECURITY_HUB</code>. </p>"""
    target_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The target account ID, organizational unit ID, or the root ID for which the association is retrieved. </p>"""
    target_type: NotRequired["aws_sdk_securityhub.types.target_type.TargetType"]
    """<p> Specifies whether the target is an Amazon Web Services account, organizational unit, or the organization root. </p>"""
    association_type: NotRequired[
        "aws_sdk_securityhub.types.association_type.AssociationType"
    ]
    """<p> Indicates whether the association between the specified target and the configuration was directly applied by the Security Hub CSPM delegated administrator or inherited from a parent. </p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p> The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated. </p>"""
    association_status: NotRequired[
        "aws_sdk_securityhub.types.configuration_policy_association_status.ConfigurationPolicyAssociationStatus"
    ]
    """<p> The current status of the association between the specified target and the configuration. </p>"""
    association_status_message: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The explanation for a <code>FAILED</code> value for <code>AssociationStatus</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationPolicyAssociationResponse) -> dict:
    out: dict = {}
    if "configuration_policy_id" in value:
        out["ConfigurationPolicyId"] = value["configuration_policy_id"]
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "target_type" in value:
        import aws_sdk_securityhub.types.target_type

        out["TargetType"] = aws_sdk_securityhub.types.target_type.serialize_json(
            value["target_type"]
        )
    if "association_type" in value:
        import aws_sdk_securityhub.types.association_type

        out["AssociationType"] = (
            aws_sdk_securityhub.types.association_type.serialize_json(
                value["association_type"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["UpdatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "association_status" in value:
        import aws_sdk_securityhub.types.configuration_policy_association_status

        out["AssociationStatus"] = (
            aws_sdk_securityhub.types.configuration_policy_association_status.serialize_json(
                value["association_status"]
            )
        )
    if "association_status_message" in value:
        out["AssociationStatusMessage"] = value["association_status_message"]
    return out


def deserialize_json(data: dict) -> GetConfigurationPolicyAssociationResponse:
    out: GetConfigurationPolicyAssociationResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicyId" in data:
        out["configuration_policy_id"] = data["ConfigurationPolicyId"]
    if "TargetId" in data:
        out["target_id"] = data["TargetId"]
    if "TargetType" in data:
        import aws_sdk_securityhub.types.target_type

        out["target_type"] = aws_sdk_securityhub.types.target_type.deserialize_json(
            data["TargetType"]
        )
    if "AssociationType" in data:
        import aws_sdk_securityhub.types.association_type

        out["association_type"] = (
            aws_sdk_securityhub.types.association_type.deserialize_json(
                data["AssociationType"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["updated_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "AssociationStatus" in data:
        import aws_sdk_securityhub.types.configuration_policy_association_status

        out["association_status"] = (
            aws_sdk_securityhub.types.configuration_policy_association_status.deserialize_json(
                data["AssociationStatus"]
            )
        )
    if "AssociationStatusMessage" in data:
        out["association_status_message"] = data["AssociationStatusMessage"]
    return out
