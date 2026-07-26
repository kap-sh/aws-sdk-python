"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeSlackUserIdentitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.max_results
    import capo_chatbot.types.pagination_token


class DescribeSlackUserIdentitiesRequest(TypedDict, closed=True):
    chat_configuration_arn: NotRequired[
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration associated with the user identities to describe.</p>"""
    next_token: NotRequired["capo_chatbot.types.pagination_token.PaginationToken"]
    """<p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>"""
    max_results: NotRequired["capo_chatbot.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlackUserIdentitiesRequest) -> dict:
    out: dict = {}
    if "chat_configuration_arn" in value:
        out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeSlackUserIdentitiesRequest:
    out: DescribeSlackUserIdentitiesRequest = {}  # type: ignore[typeddict-item]
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
