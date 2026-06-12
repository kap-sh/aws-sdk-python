"""Generated from Smithy shape ``com.amazonaws.chatbot#ListTeamsChannelConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.pagination_token
    import aws_sdk_chatbot.types.team_channel_configurations_list


class ListTeamsChannelConfigurationsResult(TypedDict):
    next_token: NotRequired["aws_sdk_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""
    team_channel_configurations: NotRequired[
        "aws_sdk_chatbot.types.team_channel_configurations_list.TeamChannelConfigurationsList"
    ]
    """<p>A list of AWS Chatbot channel configurations for Microsoft Teams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTeamsChannelConfigurationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "team_channel_configurations" in value:
        import aws_sdk_chatbot.types.team_channel_configurations_list

        out["TeamChannelConfigurations"] = (
            aws_sdk_chatbot.types.team_channel_configurations_list.serialize_json(
                value["team_channel_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTeamsChannelConfigurationsResult:
    out: ListTeamsChannelConfigurationsResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TeamChannelConfigurations" in data:
        import aws_sdk_chatbot.types.team_channel_configurations_list

        out["team_channel_configurations"] = (
            aws_sdk_chatbot.types.team_channel_configurations_list.deserialize_json(
                data["TeamChannelConfigurations"]
            )
        )
    return out
