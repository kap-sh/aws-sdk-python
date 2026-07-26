"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
