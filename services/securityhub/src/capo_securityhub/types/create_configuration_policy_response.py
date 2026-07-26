"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConfigurationPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.policy
    import capo_securityhub.types.timestamp


class CreateConfigurationPolicyResponse(TypedDict, closed=True):
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the configuration policy. </p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The universally unique identifier (UUID) of the configuration policy. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the configuration policy. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The description of the configuration policy. </p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated. </p>"""
    created_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> The date and time, in UTC and ISO 8601 format, that the configuration policy was created. </p>"""
    configuration_policy: NotRequired["capo_securityhub.types.policy.Policy"]
    """<p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If the request included a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If the request included a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationPolicyResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "created_at" in value:
        import capo_securityhub.types.timestamp

        out["CreatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "configuration_policy" in value:
        import capo_securityhub.types.policy

        out["ConfigurationPolicy"] = capo_securityhub.types.policy.serialize_json(
            value["configuration_policy"]
        )
    return out


def deserialize_json(data: dict) -> CreateConfigurationPolicyResponse:
    out: CreateConfigurationPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "UpdatedAt" in data:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "CreatedAt" in data:
        import capo_securityhub.types.timestamp

        out["created_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "ConfigurationPolicy" in data:
        import capo_securityhub.types.policy

        out["configuration_policy"] = capo_securityhub.types.policy.deserialize_json(
            data["ConfigurationPolicy"]
        )
    return out
