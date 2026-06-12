"""Generated from Smithy shape ``com.amazonaws.connect#ListLexBotsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.lex_bots_list
    import aws_sdk_connect.types.next_token


class ListLexBotsResponse(TypedDict):
    lex_bots: NotRequired["aws_sdk_connect.types.lex_bots_list.LexBotsList"]
    """<p>The names and Amazon Web Services Regions of the Amazon Lex bots associated with the specified instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLexBotsResponse) -> dict:
    out: dict = {}
    if "lex_bots" in value:
        import aws_sdk_connect.types.lex_bots_list

        out["LexBots"] = aws_sdk_connect.types.lex_bots_list.serialize_json(
            value["lex_bots"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLexBotsResponse:
    out: ListLexBotsResponse = {}  # type: ignore[typeddict-item]
    if "LexBots" in data:
        import aws_sdk_connect.types.lex_bots_list

        out["lex_bots"] = aws_sdk_connect.types.lex_bots_list.deserialize_json(
            data["LexBots"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
