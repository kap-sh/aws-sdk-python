"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositionRelationshipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class CompositionRelationshipItem(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositionRelationshipItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CompositionRelationshipItem:
    out: CompositionRelationshipItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
