"""Generated from Smithy shape ``com.amazonaws.entityresolution#AddPolicyStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.statement_action_list
    import aws_sdk_entityresolution.types.statement_condition
    import aws_sdk_entityresolution.types.statement_effect
    import aws_sdk_entityresolution.types.statement_id
    import aws_sdk_entityresolution.types.statement_principal_list
    import aws_sdk_entityresolution.types.venice_global_arn


class AddPolicyStatementInput(TypedDict, closed=True):
    arn: "aws_sdk_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The Amazon Resource Name (ARN) of the resource that will be accessed by the principal.</p>"""
    statement_id: "aws_sdk_entityresolution.types.statement_id.StatementId"
    """<p>A statement identifier that differentiates the statement from others in the same policy.</p>"""
    effect: "aws_sdk_entityresolution.types.statement_effect.StatementEffect"
    """<p>Determines whether the permissions specified in the policy are to be allowed (<code>Allow</code>) or denied (<code>Deny</code>).</p> <important> <p> If you set the value of the <code>effect</code> parameter to <code>Deny</code> for the <code>AddPolicyStatement</code> operation, you must also set the value of the <code>effect</code> parameter in the <code>policy</code> to <code>Deny</code> for the <code>PutPolicy</code> operation.</p> </important>"""
    action: "aws_sdk_entityresolution.types.statement_action_list.StatementActionList"
    """<p>The action that the principal can use on the resource. </p> <p>For example, <code>entityresolution:GetIdMappingJob</code>, <code>entityresolution:GetMatchingJob</code>.</p>"""
    principal: (
        "aws_sdk_entityresolution.types.statement_principal_list.StatementPrincipalList"
    )
    """<p>The Amazon Web Services service or Amazon Web Services account that can access the resource defined as ARN.</p>"""
    condition: NotRequired[
        "aws_sdk_entityresolution.types.statement_condition.StatementCondition"
    ]
    """<p>A set of condition keys that you can use in key policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPolicyStatementInput) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.statement_effect

    out["effect"] = aws_sdk_entityresolution.types.statement_effect.serialize_json(
        value["effect"]
    )
    import aws_sdk_entityresolution.types.statement_action_list

    out["action"] = aws_sdk_entityresolution.types.statement_action_list.serialize_json(
        value["action"]
    )
    import aws_sdk_entityresolution.types.statement_principal_list

    out["principal"] = (
        aws_sdk_entityresolution.types.statement_principal_list.serialize_json(
            value["principal"]
        )
    )
    if "condition" in value:
        out["condition"] = value["condition"]
    return out


def deserialize_json(data: dict) -> AddPolicyStatementInput:
    out: AddPolicyStatementInput = {}  # type: ignore[typeddict-item]
    if "effect" in data:
        import aws_sdk_entityresolution.types.statement_effect

        out["effect"] = (
            aws_sdk_entityresolution.types.statement_effect.deserialize_json(
                data["effect"]
            )
        )
    else:
        raise DeserializationError("AddPolicyStatementInput.effect required")
    if "action" in data:
        import aws_sdk_entityresolution.types.statement_action_list

        out["action"] = (
            aws_sdk_entityresolution.types.statement_action_list.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("AddPolicyStatementInput.action required")
    if "principal" in data:
        import aws_sdk_entityresolution.types.statement_principal_list

        out["principal"] = (
            aws_sdk_entityresolution.types.statement_principal_list.deserialize_json(
                data["principal"]
            )
        )
    else:
        raise DeserializationError("AddPolicyStatementInput.principal required")
    if "condition" in data:
        out["condition"] = data["condition"]
    return out
