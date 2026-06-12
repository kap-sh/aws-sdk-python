"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateConfigurationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.policy


class UpdateConfigurationPolicyRequest(TypedDict):
    identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of the configuration policy. </p>"""
    updated_reason: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The reason for updating the configuration policy. </p>"""
    configuration_policy: NotRequired["aws_sdk_securityhub.types.policy.Policy"]
    """<p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p> <p>When updating a configuration policy, provide a complete list of standards that you want to enable and a complete list of controls that you want to enable or disable. The updated configuration replaces the current configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationPolicyRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "updated_reason" in value:
        out["UpdatedReason"] = value["updated_reason"]
    if "configuration_policy" in value:
        import aws_sdk_securityhub.types.policy

        out["ConfigurationPolicy"] = aws_sdk_securityhub.types.policy.serialize_json(
            value["configuration_policy"]
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationPolicyRequest:
    out: UpdateConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "UpdatedReason" in data:
        out["updated_reason"] = data["UpdatedReason"]
    if "ConfigurationPolicy" in data:
        import aws_sdk_securityhub.types.policy

        out["configuration_policy"] = aws_sdk_securityhub.types.policy.deserialize_json(
            data["ConfigurationPolicy"]
        )
    return out
