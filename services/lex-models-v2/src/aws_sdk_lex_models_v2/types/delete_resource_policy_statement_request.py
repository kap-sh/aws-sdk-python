"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteResourcePolicyStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.amazon_resource_name
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.revision_id


class DeleteResourcePolicyStatementRequest(TypedDict):
    resource_arn: "aws_sdk_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>"""
    statement_id: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the statement (SID) to delete from the policy.</p>"""
    expected_revision_id: NotRequired[
        "aws_sdk_lex_models_v2.types.revision_id.RevisionId"
    ]
    """<p>The identifier of the revision of the policy to delete the statement from. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex removes the current contents of the statement. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyStatementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyStatementRequest:
    out: DeleteResourcePolicyStatementRequest = {}  # type: ignore[typeddict-item]
    return out
