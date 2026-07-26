"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.venice_global_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The ARN of the resource for which you want to view tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
