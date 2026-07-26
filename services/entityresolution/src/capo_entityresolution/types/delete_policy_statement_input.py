"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeletePolicyStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.statement_id
    import capo_entityresolution.types.venice_global_arn


class DeletePolicyStatementInput(TypedDict, closed=True):
    arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The ARN of the resource for which the policy need to be deleted.</p>"""
    statement_id: "capo_entityresolution.types.statement_id.StatementId"
    """<p>A statement identifier that differentiates the statement from others in the same policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyStatementInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePolicyStatementInput:
    out: DeletePolicyStatementInput = {}  # type: ignore[typeddict-item]
    return out
