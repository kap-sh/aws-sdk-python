"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeSlackUserIdentitiesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.pagination_token
    import aws_sdk_chatbot.types.slack_user_identities_list


class DescribeSlackUserIdentitiesResult(TypedDict):
    slack_user_identities: NotRequired[
        "aws_sdk_chatbot.types.slack_user_identities_list.SlackUserIdentitiesList"
    ]
    """<p>A list of Slack User Identities.</p>"""
    next_token: NotRequired["aws_sdk_chatbot.types.pagination_token.PaginationToken"]
    """<p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlackUserIdentitiesResult) -> dict:
    out: dict = {}
    if "slack_user_identities" in value:
        import aws_sdk_chatbot.types.slack_user_identities_list

        out["SlackUserIdentities"] = (
            aws_sdk_chatbot.types.slack_user_identities_list.serialize_json(
                value["slack_user_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSlackUserIdentitiesResult:
    out: DescribeSlackUserIdentitiesResult = {}  # type: ignore[typeddict-item]
    if "SlackUserIdentities" in data:
        import aws_sdk_chatbot.types.slack_user_identities_list

        out["slack_user_identities"] = (
            aws_sdk_chatbot.types.slack_user_identities_list.deserialize_json(
                data["SlackUserIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
