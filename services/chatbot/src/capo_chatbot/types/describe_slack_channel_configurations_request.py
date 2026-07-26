"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeSlackChannelConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.max_results
    import capo_chatbot.types.pagination_token


class DescribeSlackChannelConfigurationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_chatbot.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>"""
    next_token: NotRequired["capo_chatbot.types.pagination_token.PaginationToken"]
    """<p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>"""
    chat_configuration_arn: NotRequired[
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    ]
    """<p>An optional Amazon Resource Name (ARN) of a SlackChannelConfiguration to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlackChannelConfigurationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "chat_configuration_arn" in value:
        out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DescribeSlackChannelConfigurationsRequest:
    out: DescribeSlackChannelConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    return out
