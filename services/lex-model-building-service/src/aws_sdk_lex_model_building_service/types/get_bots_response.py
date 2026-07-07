"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_metadata_list
    import aws_sdk_lex_model_building_service.types.next_token


class GetBotsResponse(TypedDict, closed=True):
    bots: NotRequired[
        "aws_sdk_lex_model_building_service.types.bot_metadata_list.BotMetadataList"
    ]
    """<p>An array of <code>botMetadata</code> objects, with one entry for each bot. </p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of bots. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotsResponse) -> dict:
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


def deserialize_json(data: dict) -> GetBotsResponse:
    out: GetBotsResponse = {}  # type: ignore[typeddict-item]
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
