"""Generated from Smithy shape ``com.amazonaws.tnb#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.tnb_resource_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_tnb.types.tnb_resource_arn.TNBResourceArn"
    """<p>Resource ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
