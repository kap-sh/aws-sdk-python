"""Generated from Smithy shape ``com.amazonaws.inspector2#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_inspector2.types.arn.Arn"
    """<p>The Amazon resource number (ARN) of the resource to list tags of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
