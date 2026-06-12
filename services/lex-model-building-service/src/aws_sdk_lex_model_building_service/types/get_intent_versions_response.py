"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetIntentVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.intent_metadata_list
    import aws_sdk_lex_model_building_service.types.next_token


class GetIntentVersionsResponse(TypedDict):
    intents: NotRequired[
        "aws_sdk_lex_model_building_service.types.intent_metadata_list.IntentMetadataList"
    ]
    """<p>An array of <code>IntentMetadata</code> objects, one for each numbered version of the intent plus one for the <code>$LATEST</code> version.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntentVersionsResponse) -> dict:
    out: dict = {}
    if "intents" in value:
        import aws_sdk_lex_model_building_service.types.intent_metadata_list

        out["intents"] = (
            aws_sdk_lex_model_building_service.types.intent_metadata_list.serialize_json(
                value["intents"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetIntentVersionsResponse:
    out: GetIntentVersionsResponse = {}  # type: ignore[typeddict-item]
    if "intents" in data:
        import aws_sdk_lex_model_building_service.types.intent_metadata_list

        out["intents"] = (
            aws_sdk_lex_model_building_service.types.intent_metadata_list.deserialize_json(
                data["intents"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
