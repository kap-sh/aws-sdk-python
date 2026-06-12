"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatePermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.permission_conditions
    import aws_sdk_qbusiness.types.principal_role_arn
    import aws_sdk_qbusiness.types.q_iam_actions
    import aws_sdk_qbusiness.types.statement_id

class AssociatePermissionRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    statement_id: "aws_sdk_qbusiness.types.statement_id.StatementId"
    """<p>A unique identifier for the policy statement.</p>"""
    actions: "aws_sdk_qbusiness.types.q_iam_actions.QIamActions"
    """<p>The list of Amazon Q Business actions that the ISV is allowed to perform.</p>"""
    conditions: NotRequired["aws_sdk_qbusiness.types.permission_conditions.PermissionConditions"]
    """<p>The conditions that restrict when the permission is effective. These conditions can be used to limit the permission based on specific attributes of the request.</p>"""
    principal: "aws_sdk_qbusiness.types.principal_role_arn.PrincipalRoleArn"
    """<p>The Amazon Resource Name of the IAM role for the ISV that is being granted permission.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssociatePermissionRequest) -> dict:
    out: dict = {}
    out["statementId"] = value["statement_id"]
    import aws_sdk_qbusiness.types.q_iam_actions
    out["actions"] = aws_sdk_qbusiness.types.q_iam_actions.serialize_json(value["actions"])
    if "conditions" in value:
        import aws_sdk_qbusiness.types.permission_conditions
        out["conditions"] = aws_sdk_qbusiness.types.permission_conditions.serialize_json(value["conditions"])
    out["principal"] = value["principal"]
    return out


def deserialize_json(data: dict) -> AssociatePermissionRequest:
    out: AssociatePermissionRequest = {}  # type: ignore[typeddict-item]
    if "statementId" in data:
        out["statement_id"] = data["statementId"]
    else:
        raise DeserializationError("AssociatePermissionRequest.statement_id required")
    if "actions" in data:
        import aws_sdk_qbusiness.types.q_iam_actions
        out["actions"] = aws_sdk_qbusiness.types.q_iam_actions.deserialize_json(data["actions"])
    else:
        raise DeserializationError("AssociatePermissionRequest.actions required")
    if "conditions" in data:
        import aws_sdk_qbusiness.types.permission_conditions
        out["conditions"] = aws_sdk_qbusiness.types.permission_conditions.deserialize_json(data["conditions"])
    if "principal" in data:
        out["principal"] = data["principal"]
    else:
        raise DeserializationError("AssociatePermissionRequest.principal required")
    return out