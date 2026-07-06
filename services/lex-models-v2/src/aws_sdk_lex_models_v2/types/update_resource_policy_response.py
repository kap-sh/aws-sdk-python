"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.amazon_resource_name
    import aws_sdk_lex_models_v2.types.revision_id


class UpdateResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>"""
    revision_id: NotRequired["aws_sdk_lex_models_v2.types.revision_id.RevisionId"]
    """<p>The current revision of the resource policy. Use the revision ID to make sure that you are updating the most current version of a resource policy when you add a policy statement to a resource, delete a resource, or update a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> UpdateResourcePolicyResponse:
    out: UpdateResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    return out
