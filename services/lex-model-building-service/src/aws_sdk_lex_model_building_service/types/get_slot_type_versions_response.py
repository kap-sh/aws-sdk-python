"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetSlotTypeVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.next_token
    import aws_sdk_lex_model_building_service.types.slot_type_metadata_list


class GetSlotTypeVersionsResponse(TypedDict, closed=True):
    slot_types: NotRequired[
        "aws_sdk_lex_model_building_service.types.slot_type_metadata_list.SlotTypeMetadataList"
    ]
    """<p>An array of <code>SlotTypeMetadata</code> objects, one for each numbered version of the slot type plus one for the <code>$LATEST</code> version.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSlotTypeVersionsResponse) -> dict:
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


def deserialize_json(data: dict) -> GetSlotTypeVersionsResponse:
    out: GetSlotTypeVersionsResponse = {}  # type: ignore[typeddict-item]
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
