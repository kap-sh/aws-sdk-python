"""Generated from Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsConfiguredTeamsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.configured_teams_list
    import aws_sdk_chatbot.types.pagination_token


class ListMicrosoftTeamsConfiguredTeamsResult(TypedDict, closed=True):
    configured_teams: NotRequired[
        "aws_sdk_chatbot.types.configured_teams_list.ConfiguredTeamsList"
    ]
    """<p>A list of teams in Microsoft Teams that are configured with AWS Chatbot.</p>"""
    next_token: NotRequired["aws_sdk_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrosoftTeamsConfiguredTeamsResult) -> dict:
    out: dict = {}
    if "configured_teams" in value:
        import aws_sdk_chatbot.types.configured_teams_list

        out["ConfiguredTeams"] = (
            aws_sdk_chatbot.types.configured_teams_list.serialize_json(
                value["configured_teams"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMicrosoftTeamsConfiguredTeamsResult:
    out: ListMicrosoftTeamsConfiguredTeamsResult = {}  # type: ignore[typeddict-item]
    if "ConfiguredTeams" in data:
        import aws_sdk_chatbot.types.configured_teams_list

        out["configured_teams"] = (
            aws_sdk_chatbot.types.configured_teams_list.deserialize_json(
                data["ConfiguredTeams"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
