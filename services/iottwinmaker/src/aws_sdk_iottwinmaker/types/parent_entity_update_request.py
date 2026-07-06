"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ParentEntityUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.parent_entity_id
    import aws_sdk_iottwinmaker.types.parent_entity_update_type


class ParentEntityUpdateRequest(TypedDict, closed=True):
    update_type: (
        "aws_sdk_iottwinmaker.types.parent_entity_update_type.ParentEntityUpdateType"
    )
    """<p>The type of the update.</p>"""
    parent_entity_id: NotRequired[
        "aws_sdk_iottwinmaker.types.parent_entity_id.ParentEntityId"
    ]
    """<p>The ID of the parent entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentEntityUpdateRequest) -> dict:
    out: dict = {}
    out["updateType"] = value["update_type"]
    if "parent_entity_id" in value:
        out["parentEntityId"] = value["parent_entity_id"]
    return out


def deserialize_json(data: dict) -> ParentEntityUpdateRequest:
    out: ParentEntityUpdateRequest = {}  # type: ignore[typeddict-item]
    if "updateType" in data:
        out["update_type"] = data["updateType"]
    else:
        raise DeserializationError("ParentEntityUpdateRequest.update_type required")
    if "parentEntityId" in data:
        out["parent_entity_id"] = data["parentEntityId"]
    return out
