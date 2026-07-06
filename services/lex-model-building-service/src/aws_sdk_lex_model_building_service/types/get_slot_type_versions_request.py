"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetSlotTypeVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.max_results
    import aws_sdk_lex_model_building_service.types.next_token
    import aws_sdk_lex_model_building_service.types.slot_type_name


class GetSlotTypeVersionsRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.slot_type_name.SlotTypeName"
    """<p>The name of the slot type for which versions should be returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>"""
    max_results: NotRequired[
        "aws_sdk_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of slot type versions to return in the response. The default is 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSlotTypeVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSlotTypeVersionsRequest:
    out: GetSlotTypeVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
