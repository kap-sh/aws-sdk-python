"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p>"""
    tag_keys: "capo_kafkaconnect.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags that you want to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
