"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.association_arn
    import aws_sdk_codeguru_reviewer.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_codeguru_reviewer.types.association_arn.AssociationArn"
    """<p>The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\">ListRepositoryAssociations</a>.</p>"""
    tag_keys: "aws_sdk_codeguru_reviewer.types.tag_key_list.TagKeyList"
    """<p>A list of the keys for each tag you want to remove from an associated repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
