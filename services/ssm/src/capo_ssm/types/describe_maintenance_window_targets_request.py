"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_filter_list
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_max_results
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowTargetsRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window whose targets should be retrieved.</p>"""
    filters: NotRequired[
        "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
    ]
    """<p>Optional filters that can be used to narrow down the scope of the returned window targets. The supported filter keys are <code>Type</code>, <code>WindowTargetId</code>, and <code>OwnerInformation</code>.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowTargetsRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    if "filters" in value:
        import capo_ssm.types.maintenance_window_filter_list

        out["Filters"] = (
            capo_ssm.types.maintenance_window_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowTargetsRequest:
    out: DescribeMaintenanceWindowTargetsRequest = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError(
            "DescribeMaintenanceWindowTargetsRequest.window_id required"
        )
    if "Filters" in data:
        import capo_ssm.types.maintenance_window_filter_list

        out["filters"] = (
            capo_ssm.types.maintenance_window_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
