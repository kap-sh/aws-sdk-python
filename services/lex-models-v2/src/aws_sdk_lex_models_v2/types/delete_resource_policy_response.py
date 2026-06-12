"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.amazon_resource_name
    import aws_sdk_lex_models_v2.types.revision_id


class DeleteResourcePolicyResponse(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy was deleted from.</p>"""
    revision_id: NotRequired["aws_sdk_lex_models_v2.types.revision_id.RevisionId"]
    """<p>The current revision of the resource policy. Use the revision ID to make sure that you are updating the most current version of a resource policy when you add a policy statement to a resource, delete a resource, or update a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    return out
