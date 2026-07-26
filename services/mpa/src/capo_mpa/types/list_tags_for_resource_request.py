"""Generated from Smithy shape ``com.amazonaws.mpa#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
