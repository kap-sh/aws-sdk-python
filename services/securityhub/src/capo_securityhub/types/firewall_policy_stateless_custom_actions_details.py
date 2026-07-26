"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatelessCustomActionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.stateless_custom_action_definition


class FirewallPolicyStatelessCustomActionsDetails(TypedDict, closed=True):
    action_definition: NotRequired[
        "capo_securityhub.types.stateless_custom_action_definition.StatelessCustomActionDefinition"
    ]
    """<p>The definition of the custom action.</p>"""
    action_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the custom action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatelessCustomActionsDetails) -> dict:
    out: dict = {}
    if "action_definition" in value:
        import capo_securityhub.types.stateless_custom_action_definition

        out["ActionDefinition"] = (
            capo_securityhub.types.stateless_custom_action_definition.serialize_json(
                value["action_definition"]
            )
        )
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    return out


def deserialize_json(data: dict) -> FirewallPolicyStatelessCustomActionsDetails:
    out: FirewallPolicyStatelessCustomActionsDetails = {}  # type: ignore[typeddict-item]
    if "ActionDefinition" in data:
        import capo_securityhub.types.stateless_custom_action_definition

        out["action_definition"] = (
            capo_securityhub.types.stateless_custom_action_definition.deserialize_json(
                data["ActionDefinition"]
            )
        )
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    return out
