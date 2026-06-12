"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.max_results
    import aws_sdk_lex_model_building_service.types.next_token


class GetBotVersionsRequest(TypedDict):
    name: "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot for which versions should be returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. </p>"""
    max_results: NotRequired[
        "aws_sdk_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of bot versions to return in the response. The default is 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotVersionsRequest:
    out: GetBotVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
