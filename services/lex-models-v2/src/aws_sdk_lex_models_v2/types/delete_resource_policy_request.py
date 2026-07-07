"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.amazon_resource_name
    import aws_sdk_lex_models_v2.types.revision_id


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that has the resource policy attached.</p>"""
    expected_revision_id: NotRequired[
        "aws_sdk_lex_models_v2.types.revision_id.RevisionId"
    ]
    """<p>The identifier of the revision to edit. If this ID doesn't match the current revision number, Amazon Lex returns an exception</p> <p>If you don't specify a revision ID, Amazon Lex will delete the current policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
