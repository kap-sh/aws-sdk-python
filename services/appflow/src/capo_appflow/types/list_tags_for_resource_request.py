"""Generated from Smithy shape ``com.amazonaws.appflow#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_appflow.types.arn.ARN"
    """<p> The Amazon Resource Name (ARN) of the specified flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
