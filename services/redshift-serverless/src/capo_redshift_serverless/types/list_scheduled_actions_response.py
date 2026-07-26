"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListScheduledActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.pagination_token
    import capo_redshift_serverless.types.scheduled_actions_list


class ListScheduledActionsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    scheduled_actions: NotRequired[
        "capo_redshift_serverless.types.scheduled_actions_list.ScheduledActionsList"
    ]
    """<p>All of the returned scheduled action association objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListScheduledActionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "scheduled_actions" in value:
        import capo_redshift_serverless.types.scheduled_actions_list

        out["scheduledActions"] = (
            capo_redshift_serverless.types.scheduled_actions_list.serialize_aws_json_1_1(
                value["scheduled_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListScheduledActionsResponse:
    out: ListScheduledActionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "scheduledActions" in data:
        import capo_redshift_serverless.types.scheduled_actions_list

        out["scheduled_actions"] = (
            capo_redshift_serverless.types.scheduled_actions_list.deserialize_aws_json_1_1(
                data["scheduledActions"]
            )
        )
    return out
