"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterfaceRelationshipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class InterfaceRelationshipSummary(TypedDict, closed=True):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model that has the interface applied to it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceRelationshipSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> InterfaceRelationshipSummary:
    out: InterfaceRelationshipSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("InterfaceRelationshipSummary.id required")
    return out
