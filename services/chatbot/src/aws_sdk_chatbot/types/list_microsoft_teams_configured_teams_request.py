"""Generated from Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsConfiguredTeamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.max_results
    import aws_sdk_chatbot.types.pagination_token


class ListMicrosoftTeamsConfiguredTeamsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_chatbot.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrosoftTeamsConfiguredTeamsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMicrosoftTeamsConfiguredTeamsRequest:
    out: ListMicrosoftTeamsConfiguredTeamsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
