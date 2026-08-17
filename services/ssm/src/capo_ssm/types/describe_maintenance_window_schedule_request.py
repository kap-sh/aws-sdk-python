"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_resource_type
    import capo_ssm.types.maintenance_window_search_max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_orchestrator_filter_list
    import capo_ssm.types.targets


class DescribeMaintenanceWindowScheduleRequest(TypedDict, closed=True):
    window_id: NotRequired["capo_ssm.types.maintenance_window_id.MaintenanceWindowId"]
    """<p>The ID of the maintenance window to retrieve information about.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The managed node ID or key-value pair to retrieve information about.</p>"""
    resource_type: NotRequired[
        "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
    ]
    """<p>The type of resource you want to retrieve information about. For example, <code>INSTANCE</code>.</p>"""
    filters: NotRequired[
        "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
    ]
    """<p>Filters used to limit the range of results. For example, you can limit maintenance window executions to only those scheduled before or after a certain date and time.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.maintenance_window_search_max_results.MaintenanceWindowSearchMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowScheduleRequest) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "resource_type" in value:
        import capo_ssm.types.maintenance_window_resource_type

        out["ResourceType"] = (
            capo_ssm.types.maintenance_window_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "filters" in value:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["Filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowScheduleRequest:
    out: DescribeMaintenanceWindowScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("ResourceType") is not None:
        import capo_ssm.types.maintenance_window_resource_type

        out["resource_type"] = (
            capo_ssm.types.maintenance_window_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if data.get("Filters") is not None:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
