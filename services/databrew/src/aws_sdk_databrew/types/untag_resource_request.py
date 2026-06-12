"""Generated from Smithy shape ``com.amazonaws.databrew#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_databrew.types.arn.Arn"
    """<p>A DataBrew resource from which you want to remove a tag or tags. The value for this parameter is an Amazon Resource Name (ARN). </p>"""
    tag_keys: "aws_sdk_databrew.types.tag_key_list.TagKeyList"
    """<p>The tag keys (names) of one or more tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
