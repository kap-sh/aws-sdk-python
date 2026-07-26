"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_alias_metadata_list
    import capo_lex_model_building_service.types.next_token


class GetBotAliasesResponse(TypedDict, closed=True):
    bot_aliases: NotRequired[
        "capo_lex_model_building_service.types.bot_alias_metadata_list.BotAliasMetadataList"
    ]
    """<p>An array of <code>BotAliasMetadata</code> objects, each describing a bot alias.</p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotAliasesResponse) -> dict:
    out: dict = {}
    if "bot_aliases" in value:
        import capo_lex_model_building_service.types.bot_alias_metadata_list

        out["BotAliases"] = (
            capo_lex_model_building_service.types.bot_alias_metadata_list.serialize_json(
                value["bot_aliases"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBotAliasesResponse:
    out: GetBotAliasesResponse = {}  # type: ignore[typeddict-item]
    if "BotAliases" in data:
        import capo_lex_model_building_service.types.bot_alias_metadata_list

        out["bot_aliases"] = (
            capo_lex_model_building_service.types.bot_alias_metadata_list.deserialize_json(
                data["BotAliases"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
