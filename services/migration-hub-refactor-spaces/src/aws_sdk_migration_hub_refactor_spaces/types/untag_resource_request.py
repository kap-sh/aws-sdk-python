"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.string
    import aws_sdk_migration_hub_refactor_spaces.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_migration_hub_refactor_spaces.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource. </p>"""
    tag_keys: "aws_sdk_migration_hub_refactor_spaces.types.tag_keys.TagKeys"
    """<p>The list of keys of the tags to be removed from the resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
