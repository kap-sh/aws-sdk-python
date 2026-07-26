"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.accept_action
    import capo_mailmanager.types.policy_conditions


class PolicyStatement(TypedDict, closed=True):
    conditions: "capo_mailmanager.types.policy_conditions.PolicyConditions"
    """<p>The list of conditions to apply to incoming messages for filtering email traffic.</p>"""
    action: "capo_mailmanager.types.accept_action.AcceptAction"
    """<p>The action that informs a traffic policy resource to either allow or block the email if it matches a condition in the policy statement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStatement) -> dict:
    out: dict = {}
    import capo_mailmanager.types.policy_conditions

    out["Conditions"] = capo_mailmanager.types.policy_conditions.serialize_aws_json_1_0(
        value["conditions"]
    )
    import capo_mailmanager.types.accept_action

    out["Action"] = capo_mailmanager.types.accept_action.serialize_aws_json_1_0(
        value["action"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyStatement:
    out: PolicyStatement = {}  # type: ignore[typeddict-item]
    if "Conditions" in data:
        import capo_mailmanager.types.policy_conditions

        out["conditions"] = (
            capo_mailmanager.types.policy_conditions.deserialize_aws_json_1_0(
                data["Conditions"]
            )
        )
    else:
        raise DeserializationError("PolicyStatement.conditions required")
    if "Action" in data:
        import capo_mailmanager.types.accept_action

        out["action"] = capo_mailmanager.types.accept_action.deserialize_aws_json_1_0(
            data["Action"]
        )
    else:
        raise DeserializationError("PolicyStatement.action required")
    return out
