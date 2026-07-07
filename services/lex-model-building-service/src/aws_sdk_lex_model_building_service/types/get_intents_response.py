"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetIntentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.intent_metadata_list
    import aws_sdk_lex_model_building_service.types.next_token


class GetIntentsResponse(TypedDict, closed=True):
    intents: NotRequired[
        "aws_sdk_lex_model_building_service.types.intent_metadata_list.IntentMetadataList"
    ]
    """<p>An array of <code>Intent</code> objects. For more information, see <a>PutBot</a>.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>If the response is truncated, the response includes a pagination token that you can specify in your next request to fetch the next page of intents. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntentsResponse) -> dict:
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


def deserialize_json(data: dict) -> GetIntentsResponse:
    out: GetIntentsResponse = {}  # type: ignore[typeddict-item]
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
