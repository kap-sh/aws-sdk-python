"""Generated from Smithy shape ``com.amazonaws.connect#ListBotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.lex_bot_config_list
    import aws_sdk_connect.types.next_token


class ListBotsResponse(TypedDict, closed=True):
    lex_bots: NotRequired["aws_sdk_connect.types.lex_bot_config_list.LexBotConfigList"]
    """<p>The names and Amazon Web Services Regions of the Amazon Lex or Amazon Lex V2 bots associated with the specified instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsResponse) -> dict:
    out: dict = {}
    if "lex_bots" in value:
        import aws_sdk_connect.types.lex_bot_config_list

        out["LexBots"] = aws_sdk_connect.types.lex_bot_config_list.serialize_json(
            value["lex_bots"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotsResponse:
    out: ListBotsResponse = {}  # type: ignore[typeddict-item]
    if "LexBots" in data:
        import aws_sdk_connect.types.lex_bot_config_list

        out["lex_bots"] = aws_sdk_connect.types.lex_bot_config_list.deserialize_json(
            data["LexBots"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
