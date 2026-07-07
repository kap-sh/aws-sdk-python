"""Generated from Smithy shape ``com.amazonaws.rbin#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rbin.types.rule_arn
    import aws_sdk_rbin.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_rbin.types.rule_arn.RuleArn"
    """<p>The Amazon Resource Name (ARN) of the retention rule.</p>"""
    tag_keys: "aws_sdk_rbin.types.tag_key_list.TagKeyList"
    """<p>The tag keys of the tags to unassign. All tags that have the specified tag key are unassigned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
