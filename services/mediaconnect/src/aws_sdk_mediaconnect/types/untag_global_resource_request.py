"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UntagGlobalResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_string


class UntagGlobalResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the global resource to remove tags from.</p>"""
    tag_keys: NotRequired["aws_sdk_mediaconnect.types.__list_of_string.__listOfString"]
    """<p>The keys of the tags to remove from the global resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagGlobalResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagGlobalResourceRequest:
    out: UntagGlobalResourceRequest = {}  # type: ignore[typeddict-item]
    return out
