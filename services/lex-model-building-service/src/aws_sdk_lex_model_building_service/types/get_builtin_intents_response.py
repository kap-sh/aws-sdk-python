"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBuiltinIntentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.builtin_intent_metadata_list
    import aws_sdk_lex_model_building_service.types.next_token


class GetBuiltinIntentsResponse(TypedDict, closed=True):
    intents: NotRequired[
        "aws_sdk_lex_model_building_service.types.builtin_intent_metadata_list.BuiltinIntentMetadataList"
    ]
    """<p>An array of <code>builtinIntentMetadata</code> objects, one for each intent in the response.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuiltinIntentsResponse) -> dict:
    out: dict = {}
    if "intents" in value:
        import aws_sdk_lex_model_building_service.types.builtin_intent_metadata_list

        out["intents"] = (
            aws_sdk_lex_model_building_service.types.builtin_intent_metadata_list.serialize_json(
                value["intents"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBuiltinIntentsResponse:
    out: GetBuiltinIntentsResponse = {}  # type: ignore[typeddict-item]
    if "intents" in data:
        import aws_sdk_lex_model_building_service.types.builtin_intent_metadata_list

        out["intents"] = (
            aws_sdk_lex_model_building_service.types.builtin_intent_metadata_list.deserialize_json(
                data["intents"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
