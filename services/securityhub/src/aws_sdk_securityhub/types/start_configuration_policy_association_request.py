"""Generated from Smithy shape ``com.amazonaws.securityhub#StartConfigurationPolicyAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.target


class StartConfigurationPolicyAssociationRequest(TypedDict):
    configuration_policy_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of a configuration policy, the universally unique identifier (UUID) of a configuration policy, or a value of <code>SELF_MANAGED_SECURITY_HUB</code> for a self-managed configuration. </p>"""
    target: NotRequired["aws_sdk_securityhub.types.target.Target"]
    """<p> The identifier of the target account, organizational unit, or the root to associate with the specified configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConfigurationPolicyAssociationRequest) -> dict:
    out: dict = {}
    if "configuration_policy_identifier" in value:
        out["ConfigurationPolicyIdentifier"] = value["configuration_policy_identifier"]
    if "target" in value:
        import aws_sdk_securityhub.types.target

        out["Target"] = aws_sdk_securityhub.types.target.serialize_json(value["target"])
    return out


def deserialize_json(data: dict) -> StartConfigurationPolicyAssociationRequest:
    out: StartConfigurationPolicyAssociationRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicyIdentifier" in data:
        out["configuration_policy_identifier"] = data["ConfigurationPolicyIdentifier"]
    if "Target" in data:
        import aws_sdk_securityhub.types.target

        out["target"] = aws_sdk_securityhub.types.target.deserialize_json(
            data["Target"]
        )
    return out
