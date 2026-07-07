"""Generated from Smithy shape ``com.amazonaws.docdbelastic#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.arn
    import aws_sdk_docdb_elastic.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_docdb_elastic.types.arn.Arn"
    """<p>The ARN identifier of the elastic cluster resource.</p>"""
    tag_keys: "aws_sdk_docdb_elastic.types.tag_key_list.TagKeyList"
    """<p>The tag keys to be removed from the elastic cluster resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
