"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotTypeMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.slot_type_name
    import capo_lex_model_building_service.types.timestamp
    import capo_lex_model_building_service.types.version


class SlotTypeMetadata(TypedDict, closed=True):
    name: NotRequired[
        "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
    ]
    """<p>The name of the slot type.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the slot type.</p>"""
    last_updated_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the slot type was updated. When you create a resource, the creation date and last updated date are the same. </p>"""
    created_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the slot type was created.</p>"""
    version: NotRequired["capo_lex_model_building_service.types.version.Version"]
    """<p>The version of the slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_updated_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> SlotTypeMetadata:
    out: SlotTypeMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "lastUpdatedDate" in data:
        import capo_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "createdDate" in data:
        import capo_lex_model_building_service.types.timestamp

        out["created_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
