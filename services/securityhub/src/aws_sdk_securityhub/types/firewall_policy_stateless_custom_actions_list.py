"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatelessCustomActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_details

FirewallPolicyStatelessCustomActionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_details.FirewallPolicyStatelessCustomActionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatelessCustomActionsList) -> list:
    import aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FirewallPolicyStatelessCustomActionsList:
    import aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_details

    out: FirewallPolicyStatelessCustomActionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_details.deserialize_json(
                item
            )
        )
    return out
