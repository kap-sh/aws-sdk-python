"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateConfigurationPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.policy
    import aws_sdk_securityhub.types.timestamp


class UpdateConfigurationPolicyResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ARN of the configuration policy. </p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The UUID of the configuration policy. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the configuration policy. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of the configuration policy. </p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p> The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated. </p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p> The date and time, in UTC and ISO 8601 format, that the configuration policy was created. </p>"""
    configuration_policy: NotRequired["aws_sdk_securityhub.types.policy.Policy"]
    """<p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If the request included a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If the request included a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationPolicyResponse) -> dict:
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
        import aws_sdk_securityhub.types.timestamp

        out["UpdatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "created_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["CreatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "configuration_policy" in value:
        import aws_sdk_securityhub.types.policy

        out["ConfigurationPolicy"] = aws_sdk_securityhub.types.policy.serialize_json(
            value["configuration_policy"]
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationPolicyResponse:
    out: UpdateConfigurationPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "UpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["updated_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "CreatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["created_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "ConfigurationPolicy" in data:
        import aws_sdk_securityhub.types.policy

        out["configuration_policy"] = aws_sdk_securityhub.types.policy.deserialize_json(
            data["ConfigurationPolicy"]
        )
    return out
