"""Generated from Smithy shape ``com.amazonaws.datazone#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to be untagged in Amazon DataZone.</p>"""
    tag_keys: "capo_datazone.types.tag_key_list.TagKeyList"
    """<p>Specifies the tag keys for the <code>UntagResource</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
