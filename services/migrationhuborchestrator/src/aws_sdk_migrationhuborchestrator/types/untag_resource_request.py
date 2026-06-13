"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.resource_arn
    import aws_sdk_migrationhuborchestrator.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_migrationhuborchestrator.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p>"""
    tag_keys: "aws_sdk_migrationhuborchestrator.types.tag_key_list.TagKeyList"
    """<p>One or more tag keys. Specify only the tag keys, not the tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
