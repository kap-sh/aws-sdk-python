"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetIntentVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.intent_name
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.next_token


class GetIntentVersionsRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.intent_name.IntentName"
    """<p>The name of the intent for which versions should be returned.</p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>"""
    max_results: NotRequired[
        "capo_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of intent versions to return in the response. The default is 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntentVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntentVersionsRequest:
    out: GetIntentVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
