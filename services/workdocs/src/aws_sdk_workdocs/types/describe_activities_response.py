"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeActivitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.search_marker_type
    import aws_sdk_workdocs.types.user_activities


class DescribeActivitiesResponse(TypedDict):
    user_activities: NotRequired[
        "aws_sdk_workdocs.types.user_activities.UserActivities"
    ]
    """<p>The list of activities for the specified user and time period.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.search_marker_type.SearchMarkerType"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActivitiesResponse) -> dict:
    out: dict = {}
    if "user_activities" in value:
        import aws_sdk_workdocs.types.user_activities

        out["UserActivities"] = aws_sdk_workdocs.types.user_activities.serialize_json(
            value["user_activities"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeActivitiesResponse:
    out: DescribeActivitiesResponse = {}  # type: ignore[typeddict-item]
    if "UserActivities" in data:
        import aws_sdk_workdocs.types.user_activities

        out["user_activities"] = (
            aws_sdk_workdocs.types.user_activities.deserialize_json(
                data["UserActivities"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
