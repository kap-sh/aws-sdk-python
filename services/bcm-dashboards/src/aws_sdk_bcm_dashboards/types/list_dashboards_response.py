"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ListDashboardsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dashboard_reference_list
    import aws_sdk_bcm_dashboards.types.next_page_token


class ListDashboardsResponse(TypedDict):
    dashboards: (
        "aws_sdk_bcm_dashboards.types.dashboard_reference_list.DashboardReferenceList"
    )
    """<p>An array of dashboard references, containing basic information about each dashboard.</p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_dashboards.types.next_page_token.NextPageToken"
    ]
    """<p>The token to use to retrieve the next page of results. Not returned if there are no more results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDashboardsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.dashboard_reference_list

    out["dashboards"] = (
        aws_sdk_bcm_dashboards.types.dashboard_reference_list.serialize_aws_json_1_0(
            value["dashboards"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDashboardsResponse:
    out: ListDashboardsResponse = {}  # type: ignore[typeddict-item]
    if "dashboards" in data:
        import aws_sdk_bcm_dashboards.types.dashboard_reference_list

        out["dashboards"] = (
            aws_sdk_bcm_dashboards.types.dashboard_reference_list.deserialize_aws_json_1_0(
                data["dashboards"]
            )
        )
    else:
        raise DeserializationError("ListDashboardsResponse.dashboards required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
