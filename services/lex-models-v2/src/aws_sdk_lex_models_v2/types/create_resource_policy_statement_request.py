"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateResourcePolicyStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.amazon_resource_name
    import aws_sdk_lex_models_v2.types.condition_map
    import aws_sdk_lex_models_v2.types.effect
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.operation_list
    import aws_sdk_lex_models_v2.types.principal_list
    import aws_sdk_lex_models_v2.types.revision_id


class CreateResourcePolicyStatementRequest(TypedDict):
    resource_arn: "aws_sdk_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>"""
    statement_id: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the statement. The ID is the same as the <code>Sid</code> IAM property. The statement name must be unique within the policy. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_sid.html\">IAM JSON policy elements: Sid</a>. </p>"""
    effect: "aws_sdk_lex_models_v2.types.effect.Effect"
    """<p>Determines whether the statement allows or denies access to the resource.</p>"""
    principal: "aws_sdk_lex_models_v2.types.principal_list.PrincipalList"
    """<p>An IAM principal, such as an IAM user, IAM role, or Amazon Web Services services that is allowed or denied access to a resource. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html\">Amazon Web Services JSON policy elements: Principal</a>.</p>"""
    action: "aws_sdk_lex_models_v2.types.operation_list.OperationList"
    """<p>The Amazon Lex action that this policy either allows or denies. The action must apply to the resource type of the specified ARN. For more information, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlexv2.html\"> Actions, resources, and condition keys for Amazon Lex V2</a>.</p>"""
    condition: NotRequired["aws_sdk_lex_models_v2.types.condition_map.ConditionMap"]
    """<p>Specifies a condition when the policy is in effect. If the principal of the policy is a service principal, you must provide two condition blocks, one with a SourceAccount global condition key and one with a SourceArn global condition key.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html\">IAM JSON policy elements: Condition </a>.</p>"""
    expected_revision_id: NotRequired[
        "aws_sdk_lex_models_v2.types.revision_id.RevisionId"
    ]
    """<p>The identifier of the revision of the policy to edit. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourcePolicyStatementRequest) -> dict:
    out: dict = {}
    out["statementId"] = value["statement_id"]
    import aws_sdk_lex_models_v2.types.effect

    out["effect"] = aws_sdk_lex_models_v2.types.effect.serialize_json(value["effect"])
    import aws_sdk_lex_models_v2.types.principal_list

    out["principal"] = aws_sdk_lex_models_v2.types.principal_list.serialize_json(
        value["principal"]
    )
    import aws_sdk_lex_models_v2.types.operation_list

    out["action"] = aws_sdk_lex_models_v2.types.operation_list.serialize_json(
        value["action"]
    )
    if "condition" in value:
        import aws_sdk_lex_models_v2.types.condition_map

        out["condition"] = aws_sdk_lex_models_v2.types.condition_map.serialize_json(
            value["condition"]
        )
    return out


def deserialize_json(data: dict) -> CreateResourcePolicyStatementRequest:
    out: CreateResourcePolicyStatementRequest = {}  # type: ignore[typeddict-item]
    if "statementId" in data:
        out["statement_id"] = data["statementId"]
    else:
        raise DeserializationError(
            "CreateResourcePolicyStatementRequest.statement_id required"
        )
    if "effect" in data:
        import aws_sdk_lex_models_v2.types.effect

        out["effect"] = aws_sdk_lex_models_v2.types.effect.deserialize_json(
            data["effect"]
        )
    else:
        raise DeserializationError(
            "CreateResourcePolicyStatementRequest.effect required"
        )
    if "principal" in data:
        import aws_sdk_lex_models_v2.types.principal_list

        out["principal"] = aws_sdk_lex_models_v2.types.principal_list.deserialize_json(
            data["principal"]
        )
    else:
        raise DeserializationError(
            "CreateResourcePolicyStatementRequest.principal required"
        )
    if "action" in data:
        import aws_sdk_lex_models_v2.types.operation_list

        out["action"] = aws_sdk_lex_models_v2.types.operation_list.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError(
            "CreateResourcePolicyStatementRequest.action required"
        )
    if "condition" in data:
        import aws_sdk_lex_models_v2.types.condition_map

        out["condition"] = aws_sdk_lex_models_v2.types.condition_map.deserialize_json(
            data["condition"]
        )
    return out
