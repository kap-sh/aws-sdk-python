"""Generated from Smithy shape ``com.amazonaws.connect#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_connect.types.tag_key_list.TagKeyList"
    """<p>The tag keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
