"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDashboardsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.dashboard_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListDashboardsResponse(TypedDict):
    dashboard_summaries: (
        "aws_sdk_iotsitewise.types.dashboard_summaries.DashboardSummaries"
    )
    """<p>A list that summarizes each dashboard in the project.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashboardsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.dashboard_summaries

    out["dashboardSummaries"] = (
        aws_sdk_iotsitewise.types.dashboard_summaries.serialize_json(
            value["dashboard_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDashboardsResponse:
    out: ListDashboardsResponse = {}  # type: ignore[typeddict-item]
    if "dashboardSummaries" in data:
        import aws_sdk_iotsitewise.types.dashboard_summaries

        out["dashboard_summaries"] = (
            aws_sdk_iotsitewise.types.dashboard_summaries.deserialize_json(
                data["dashboardSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListDashboardsResponse.dashboard_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
