"""Generated from Smithy shape ``com.amazonaws.securityhub#StartConfigurationPolicyDisassociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.target


class StartConfigurationPolicyDisassociationRequest(TypedDict, closed=True):
    target: NotRequired["capo_securityhub.types.target.Target"]
    """<p> The identifier of the target account, organizational unit, or the root to disassociate from the specified configuration. </p>"""
    configuration_policy_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of a configuration policy, the universally unique identifier (UUID) of a configuration policy, or a value of <code>SELF_MANAGED_SECURITY_HUB</code> for a self-managed configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConfigurationPolicyDisassociationRequest) -> dict:
    out: dict = {}
    if "target" in value:
        import capo_securityhub.types.target

        out["Target"] = capo_securityhub.types.target.serialize_json(value["target"])
    if "configuration_policy_identifier" in value:
        out["ConfigurationPolicyIdentifier"] = value["configuration_policy_identifier"]
    return out


def deserialize_json(data: dict) -> StartConfigurationPolicyDisassociationRequest:
    out: StartConfigurationPolicyDisassociationRequest = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        import capo_securityhub.types.target

        out["target"] = capo_securityhub.types.target.deserialize_json(data["Target"])
    if "ConfigurationPolicyIdentifier" in data:
        out["configuration_policy_identifier"] = data["ConfigurationPolicyIdentifier"]
    return out
