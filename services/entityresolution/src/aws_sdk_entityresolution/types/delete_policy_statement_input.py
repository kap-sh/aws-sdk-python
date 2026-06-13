"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeletePolicyStatementInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.statement_id
    import aws_sdk_entityresolution.types.venice_global_arn


class DeletePolicyStatementInput(TypedDict):
    arn: "aws_sdk_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The ARN of the resource for which the policy need to be deleted.</p>"""
    statement_id: "aws_sdk_entityresolution.types.statement_id.StatementId"
    """<p>A statement identifier that differentiates the statement from others in the same policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyStatementInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePolicyStatementInput:
    out: DeletePolicyStatementInput = {}  # type: ignore[typeddict-item]
    return out
