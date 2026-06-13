"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_string


class UntagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p> The Amazon Resource Name (ARN) of the resource that you want to untag. </p>"""
    tag_keys: NotRequired["aws_sdk_mediaconnect.types.__list_of_string.__listOfString"]
    """<p>The keys of the tags to be removed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
