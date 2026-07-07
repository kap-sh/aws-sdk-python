"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.list_service_instances_filter_list
    import aws_sdk_proton.types.list_service_instances_sort_by
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.sort_order


class ListServiceInstancesInput(TypedDict, closed=True):
    service_name: NotRequired["aws_sdk_proton.types.resource_name.ResourceName"]
    """<p>The name of the service that the service instance belongs to.</p>"""
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next service in the array of service instances, after the list of service instances that was previously requested.</p>"""
    max_results: NotRequired["aws_sdk_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of service instances to list.</p>"""
    filters: NotRequired[
        "aws_sdk_proton.types.list_service_instances_filter_list.ListServiceInstancesFilterList"
    ]
    """<p>An array of filtering criteria that scope down the result list. By default, all service instances in the Amazon Web Services account are returned.</p>"""
    sort_by: NotRequired[
        "aws_sdk_proton.types.list_service_instances_sort_by.ListServiceInstancesSortBy"
    ]
    """<p>The field that the result list is sorted by.</p> <p>When you choose to sort by <code>serviceName</code>, service instances within each service are sorted by service instance name.</p> <p>Default: <code>serviceName</code> </p>"""
    sort_order: NotRequired["aws_sdk_proton.types.sort_order.SortOrder"]
    """<p>Result list sort order.</p> <p>Default: <code>ASCENDING</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstancesInput) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_proton.types.list_service_instances_filter_list

        out["filters"] = (
            aws_sdk_proton.types.list_service_instances_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstancesInput:
    out: ListServiceInstancesInput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import aws_sdk_proton.types.list_service_instances_filter_list

        out["filters"] = (
            aws_sdk_proton.types.list_service_instances_filter_list.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    return out
