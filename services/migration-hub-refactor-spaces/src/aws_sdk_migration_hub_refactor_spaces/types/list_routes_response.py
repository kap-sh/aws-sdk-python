"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListRoutesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.next_token
    import aws_sdk_migration_hub_refactor_spaces.types.route_summaries


class ListRoutesResponse(TypedDict):
    route_summary_list: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_summaries.RouteSummaries"
    ]
    """<p>The list of <code>RouteSummary</code> objects. </p>"""
    next_token: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutesResponse) -> dict:
    out: dict = {}
    if "route_summary_list" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.route_summaries

        out["RouteSummaryList"] = (
            aws_sdk_migration_hub_refactor_spaces.types.route_summaries.serialize_json(
                value["route_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoutesResponse:
    out: ListRoutesResponse = {}  # type: ignore[typeddict-item]
    if "RouteSummaryList" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.route_summaries

        out["route_summary_list"] = (
            aws_sdk_migration_hub_refactor_spaces.types.route_summaries.deserialize_json(
                data["RouteSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
