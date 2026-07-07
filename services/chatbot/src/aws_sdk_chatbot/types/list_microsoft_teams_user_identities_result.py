"""Generated from Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsUserIdentitiesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.pagination_token
    import aws_sdk_chatbot.types.teams_user_identities_list


class ListMicrosoftTeamsUserIdentitiesResult(TypedDict, closed=True):
    teams_user_identities: NotRequired[
        "aws_sdk_chatbot.types.teams_user_identities_list.TeamsUserIdentitiesList"
    ]
    """<p>User level permissions associated to a channel configuration.</p>"""
    next_token: NotRequired["aws_sdk_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrosoftTeamsUserIdentitiesResult) -> dict:
    out: dict = {}
    if "teams_user_identities" in value:
        import aws_sdk_chatbot.types.teams_user_identities_list

        out["TeamsUserIdentities"] = (
            aws_sdk_chatbot.types.teams_user_identities_list.serialize_json(
                value["teams_user_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMicrosoftTeamsUserIdentitiesResult:
    out: ListMicrosoftTeamsUserIdentitiesResult = {}  # type: ignore[typeddict-item]
    if "TeamsUserIdentities" in data:
        import aws_sdk_chatbot.types.teams_user_identities_list

        out["teams_user_identities"] = (
            aws_sdk_chatbot.types.teams_user_identities_list.deserialize_json(
                data["TeamsUserIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
