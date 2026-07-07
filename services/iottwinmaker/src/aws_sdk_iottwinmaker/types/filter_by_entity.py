"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FilterByEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.entity_id


class FilterByEntity(TypedDict, closed=True):
    entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId"
    """<p>The entity Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterByEntity) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    return out


def deserialize_json(data: dict) -> FilterByEntity:
    out: FilterByEntity = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    else:
        raise DeserializationError("FilterByEntity.entity_id required")
    return out
