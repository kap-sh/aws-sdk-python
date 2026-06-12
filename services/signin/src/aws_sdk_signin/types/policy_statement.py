"""Generated from Smithy shape ``com.amazonaws.signin#PolicyStatement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signin.types.condition_block
    import aws_sdk_signin.types.policy_actions
    import aws_sdk_signin.types.principal


class PolicyStatement(TypedDict):
    effect: NotRequired["str"]
    """Effect of the policy statement (Allow/Deny)"""
    principal: NotRequired["aws_sdk_signin.types.principal.Principal"]
    """Principal the statement applies to"""
    action: NotRequired["aws_sdk_signin.types.policy_actions.PolicyActions"]
    """Actions the statement controls"""
    resource: NotRequired["str"]
    """Resource the statement applies to"""
    condition: NotRequired["aws_sdk_signin.types.condition_block.ConditionBlock"]
    """Condition block for the statement"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyStatement) -> dict:
    out: dict = {}
    if "effect" in value:
        out["Effect"] = value["effect"]
    if "principal" in value:
        import aws_sdk_signin.types.principal

        out["Principal"] = aws_sdk_signin.types.principal.serialize_json(
            value["principal"]
        )
    if "action" in value:
        import aws_sdk_signin.types.policy_actions

        out["Action"] = aws_sdk_signin.types.policy_actions.serialize_json(
            value["action"]
        )
    if "resource" in value:
        out["Resource"] = value["resource"]
    if "condition" in value:
        import aws_sdk_signin.types.condition_block

        out["Condition"] = aws_sdk_signin.types.condition_block.serialize_json(
            value["condition"]
        )
    return out


def deserialize_json(data: dict) -> PolicyStatement:
    out: PolicyStatement = {}  # type: ignore[typeddict-item]
    if "Effect" in data:
        out["effect"] = data["Effect"]
    if "Principal" in data:
        import aws_sdk_signin.types.principal

        out["principal"] = aws_sdk_signin.types.principal.deserialize_json(
            data["Principal"]
        )
    if "Action" in data:
        import aws_sdk_signin.types.policy_actions

        out["action"] = aws_sdk_signin.types.policy_actions.deserialize_json(
            data["Action"]
        )
    if "Resource" in data:
        out["resource"] = data["Resource"]
    if "Condition" in data:
        import aws_sdk_signin.types.condition_block

        out["condition"] = aws_sdk_signin.types.condition_block.deserialize_json(
            data["Condition"]
        )
    return out
