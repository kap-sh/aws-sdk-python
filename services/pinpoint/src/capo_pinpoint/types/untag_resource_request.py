"""Generated from Smithy shape ``com.amazonaws.pinpoint#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.list_of__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_pinpoint.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: NotRequired["capo_pinpoint.types.list_of__string.ListOf__string"]
    """<p>The key of the tag to remove from the resource. To remove multiple tags, append the tagKeys parameter and argument for each additional tag to remove, separated by an ampersand (&amp;).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
