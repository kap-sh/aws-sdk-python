"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatelessCustomActionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.stateless_custom_action_definition


class FirewallPolicyStatelessCustomActionsDetails(TypedDict):
    action_definition: NotRequired[
        "aws_sdk_securityhub.types.stateless_custom_action_definition.StatelessCustomActionDefinition"
    ]
    """<p>The definition of the custom action.</p>"""
    action_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the custom action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatelessCustomActionsDetails) -> dict:
    out: dict = {}
    if "action_definition" in value:
        import aws_sdk_securityhub.types.stateless_custom_action_definition

        out["ActionDefinition"] = (
            aws_sdk_securityhub.types.stateless_custom_action_definition.serialize_json(
                value["action_definition"]
            )
        )
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    return out


def deserialize_json(data: dict) -> FirewallPolicyStatelessCustomActionsDetails:
    out: FirewallPolicyStatelessCustomActionsDetails = {}  # type: ignore[typeddict-item]
    if "ActionDefinition" in data:
        import aws_sdk_securityhub.types.stateless_custom_action_definition

        out["action_definition"] = (
            aws_sdk_securityhub.types.stateless_custom_action_definition.deserialize_json(
                data["ActionDefinition"]
            )
        )
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    return out
