"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_metadata_list
    import aws_sdk_lex_model_building_service.types.next_token


class GetBotVersionsResponse(TypedDict, closed=True):
    bots: NotRequired[
        "aws_sdk_lex_model_building_service.types.bot_metadata_list.BotMetadataList"
    ]
    """<p>An array of <code>BotMetadata</code> objects, one for each numbered version of the bot plus one for the <code>$LATEST</code> version.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotVersionsResponse) -> dict:
    out: dict = {}
    if "bots" in value:
        import aws_sdk_lex_model_building_service.types.bot_metadata_list

        out["bots"] = (
            aws_sdk_lex_model_building_service.types.bot_metadata_list.serialize_json(
                value["bots"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBotVersionsResponse:
    out: GetBotVersionsResponse = {}  # type: ignore[typeddict-item]
    if "bots" in data:
        import aws_sdk_lex_model_building_service.types.bot_metadata_list

        out["bots"] = (
            aws_sdk_lex_model_building_service.types.bot_metadata_list.deserialize_json(
                data["bots"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
