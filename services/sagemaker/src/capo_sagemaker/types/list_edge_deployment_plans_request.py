"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgeDeploymentPlansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.list_edge_deployment_plans_sort_by
    import capo_sagemaker.types.list_max_results
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListEdgeDeploymentPlansRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to need tokening.</p>"""
    max_results: NotRequired["capo_sagemaker.types.list_max_results.ListMaxResults"]
    """<p>The maximum number of results to select (50 by default).</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects edge deployment plans created after this time.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects edge deployment plans created before this time.</p>"""
    last_modified_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects edge deployment plans that were last updated after this time.</p>"""
    last_modified_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects edge deployment plans that were last updated before this time.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>Selects edge deployment plans with names containing this name.</p>"""
    device_fleet_name_contains: NotRequired[
        "capo_sagemaker.types.name_contains.NameContains"
    ]
    """<p>Selects edge deployment plans with a device fleet name containing this name.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.list_edge_deployment_plans_sort_by.ListEdgeDeploymentPlansSortBy"
    ]
    """<p>The column by which to sort the edge deployment plans. Can be one of <code>NAME</code>, <code>DEVICEFLEETNAME</code>, <code>CREATIONTIME</code>, <code>LASTMODIFIEDTIME</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The direction of the sorting (ascending or descending).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEdgeDeploymentPlansRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "device_fleet_name_contains" in value:
        out["DeviceFleetNameContains"] = value["device_fleet_name_contains"]
    if "sort_by" in value:
        import capo_sagemaker.types.list_edge_deployment_plans_sort_by

        out["SortBy"] = (
            capo_sagemaker.types.list_edge_deployment_plans_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEdgeDeploymentPlansRequest:
    out: ListEdgeDeploymentPlansRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "CreationTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "DeviceFleetNameContains" in data:
        out["device_fleet_name_contains"] = data["DeviceFleetNameContains"]
    if "SortBy" in data:
        import capo_sagemaker.types.list_edge_deployment_plans_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.list_edge_deployment_plans_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
