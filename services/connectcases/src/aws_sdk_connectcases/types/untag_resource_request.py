"""Generated from Smithy shape ``com.amazonaws.connectcases#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.arn
    import aws_sdk_connectcases.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_connectcases.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN)</p>"""
    tag_keys: "aws_sdk_connectcases.types.tag_key_list.TagKeyList"
    """<p>List of tag keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
