"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyStatement``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.accept_action
    import aws_sdk_mailmanager.types.policy_conditions


class PolicyStatement(TypedDict):
    conditions: "aws_sdk_mailmanager.types.policy_conditions.PolicyConditions"
    """<p>The list of conditions to apply to incoming messages for filtering email traffic.</p>"""
    action: "aws_sdk_mailmanager.types.accept_action.AcceptAction"
    """<p>The action that informs a traffic policy resource to either allow or block the email if it matches a condition in the policy statement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStatement) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.policy_conditions

    out["Conditions"] = (
        aws_sdk_mailmanager.types.policy_conditions.serialize_aws_json_1_0(
            value["conditions"]
        )
    )
    import aws_sdk_mailmanager.types.accept_action

    out["Action"] = aws_sdk_mailmanager.types.accept_action.serialize_aws_json_1_0(
        value["action"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyStatement:
    out: PolicyStatement = {}  # type: ignore[typeddict-item]
    if "Conditions" in data:
        import aws_sdk_mailmanager.types.policy_conditions

        out["conditions"] = (
            aws_sdk_mailmanager.types.policy_conditions.deserialize_aws_json_1_0(
                data["Conditions"]
            )
        )
    else:
        raise DeserializationError("PolicyStatement.conditions required")
    if "Action" in data:
        import aws_sdk_mailmanager.types.accept_action

        out["action"] = (
            aws_sdk_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("PolicyStatement.action required")
    return out
