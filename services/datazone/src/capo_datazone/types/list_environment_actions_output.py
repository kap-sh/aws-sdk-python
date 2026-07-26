"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentActionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.list_environment_action_summaries
    import capo_datazone.types.pagination_token


class ListEnvironmentActionsOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_datazone.types.list_environment_action_summaries.ListEnvironmentActionSummaries"
    ]
    """<p>The results of <code>ListEnvironmentActions</code>.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of environment actions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environment actions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentActions</code> to list the next set of environment actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentActionsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_datazone.types.list_environment_action_summaries

        out["items"] = (
            capo_datazone.types.list_environment_action_summaries.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentActionsOutput:
    out: ListEnvironmentActionsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_datazone.types.list_environment_action_summaries

        out["items"] = (
            capo_datazone.types.list_environment_action_summaries.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
