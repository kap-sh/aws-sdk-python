"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.association_type
    import aws_sdk_securityhub.types.configuration_policy_association_status
    import aws_sdk_securityhub.types.non_empty_string


class AssociationFilters(TypedDict, closed=True):
    configuration_policy_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN or UUID of the configuration policy. </p>"""
    association_type: NotRequired[
        "aws_sdk_securityhub.types.association_type.AssociationType"
    ]
    """<p> Indicates whether the association between a target and a configuration was directly applied by the Security Hub CSPM delegated administrator or inherited from a parent. </p>"""
    association_status: NotRequired[
        "aws_sdk_securityhub.types.configuration_policy_association_status.ConfigurationPolicyAssociationStatus"
    ]
    """<p> The current status of the association between a target and a configuration policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociationFilters) -> dict:
    out: dict = {}
    if "configuration_policy_id" in value:
        out["ConfigurationPolicyId"] = value["configuration_policy_id"]
    if "association_type" in value:
        import aws_sdk_securityhub.types.association_type

        out["AssociationType"] = (
            aws_sdk_securityhub.types.association_type.serialize_json(
                value["association_type"]
            )
        )
    if "association_status" in value:
        import aws_sdk_securityhub.types.configuration_policy_association_status

        out["AssociationStatus"] = (
            aws_sdk_securityhub.types.configuration_policy_association_status.serialize_json(
                value["association_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociationFilters:
    out: AssociationFilters = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicyId" in data:
        out["configuration_policy_id"] = data["ConfigurationPolicyId"]
    if "AssociationType" in data:
        import aws_sdk_securityhub.types.association_type

        out["association_type"] = (
            aws_sdk_securityhub.types.association_type.deserialize_json(
                data["AssociationType"]
            )
        )
    if "AssociationStatus" in data:
        import aws_sdk_securityhub.types.configuration_policy_association_status

        out["association_status"] = (
            aws_sdk_securityhub.types.configuration_policy_association_status.deserialize_json(
                data["AssociationStatus"]
            )
        )
    return out
