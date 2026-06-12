"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBuiltinSlotTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata_list
    import aws_sdk_lex_model_building_service.types.next_token


class GetBuiltinSlotTypesResponse(TypedDict):
    slot_types: NotRequired[
        "aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata_list.BuiltinSlotTypeMetadataList"
    ]
    """<p>An array of <code>BuiltInSlotTypeMetadata</code> objects, one entry for each slot type returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>If the response is truncated, the response includes a pagination token that you can use in your next request to fetch the next page of slot types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuiltinSlotTypesResponse) -> dict:
    out: dict = {}
    if "slot_types" in value:
        import aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata_list

        out["slotTypes"] = (
            aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata_list.serialize_json(
                value["slot_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBuiltinSlotTypesResponse:
    out: GetBuiltinSlotTypesResponse = {}  # type: ignore[typeddict-item]
    if "slotTypes" in data:
        import aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata_list

        out["slot_types"] = (
            aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata_list.deserialize_json(
                data["slotTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
