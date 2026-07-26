"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mediatailor.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) associated with this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
