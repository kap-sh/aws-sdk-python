"""Generated from Smithy shape ``com.amazonaws.mq#DeleteTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__list_of__string
    import capo_mq.types.__string


class DeleteTagsRequest(TypedDict, closed=True):
    resource_arn: "capo_mq.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource tag.</p>"""
    tag_keys: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>An array of tag keys to delete</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTagsRequest:
    out: DeleteTagsRequest = {}  # type: ignore[typeddict-item]
    return out
