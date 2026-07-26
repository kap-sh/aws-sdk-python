"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBuiltinSlotTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.builtin_slot_type_metadata_list
    import capo_lex_model_building_service.types.next_token


class GetBuiltinSlotTypesResponse(TypedDict, closed=True):
    slot_types: NotRequired[
        "capo_lex_model_building_service.types.builtin_slot_type_metadata_list.BuiltinSlotTypeMetadataList"
    ]
    """<p>An array of <code>BuiltInSlotTypeMetadata</code> objects, one entry for each slot type returned.</p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>If the response is truncated, the response includes a pagination token that you can use in your next request to fetch the next page of slot types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuiltinSlotTypesResponse) -> dict:
    out: dict = {}
    if "slot_types" in value:
        import capo_lex_model_building_service.types.builtin_slot_type_metadata_list

        out["slotTypes"] = (
            capo_lex_model_building_service.types.builtin_slot_type_metadata_list.serialize_json(
                value["slot_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBuiltinSlotTypesResponse:
    out: GetBuiltinSlotTypesResponse = {}  # type: ignore[typeddict-item]
    if "slotTypes" in data:
        import capo_lex_model_building_service.types.builtin_slot_type_metadata_list

        out["slot_types"] = (
            capo_lex_model_building_service.types.builtin_slot_type_metadata_list.deserialize_json(
                data["slotTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
