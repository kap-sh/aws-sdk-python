"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetSlotTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.next_token
    import aws_sdk_lex_model_building_service.types.slot_type_metadata_list


class GetSlotTypesResponse(TypedDict, closed=True):
    slot_types: NotRequired[
        "aws_sdk_lex_model_building_service.types.slot_type_metadata_list.SlotTypeMetadataList"
    ]
    """<p>An array of objects, one for each slot type, that provides information such as the name of the slot type, the version, and a description.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of slot types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSlotTypesResponse) -> dict:
    out: dict = {}
    if "slot_types" in value:
        import aws_sdk_lex_model_building_service.types.slot_type_metadata_list

        out["slotTypes"] = (
            aws_sdk_lex_model_building_service.types.slot_type_metadata_list.serialize_json(
                value["slot_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSlotTypesResponse:
    out: GetSlotTypesResponse = {}  # type: ignore[typeddict-item]
    if "slotTypes" in data:
        import aws_sdk_lex_model_building_service.types.slot_type_metadata_list

        out["slot_types"] = (
            aws_sdk_lex_model_building_service.types.slot_type_metadata_list.deserialize_json(
                data["slotTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
