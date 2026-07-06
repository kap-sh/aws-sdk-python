"""Generated from Smithy shape ``com.amazonaws.macie2#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_macie2.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>One or more tags (keys) to remove from the resource. In an HTTP request to remove multiple tags, append the tagKeys parameter and argument for each tag to remove, separated by an ampersand (&amp;).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
