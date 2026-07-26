"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to remove the tag from.</p>"""
    tag_keys: "capo_accessanalyzer.types.tag_keys.TagKeys"
    """<p>The key for the tag to add.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
