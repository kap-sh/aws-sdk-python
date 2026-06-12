"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeImportTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.describe_import_tasks_filter_list
    import aws_sdk_application_discovery_service.types.describe_import_tasks_max_results
    import aws_sdk_application_discovery_service.types.next_token


class DescribeImportTasksRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_application_discovery_service.types.describe_import_tasks_filter_list.DescribeImportTasksFilterList"
    ]
    """<p>An array of name-value pairs that you provide to filter the results for the <code>DescribeImportTask</code> request to a specific subset of results. Currently, wildcard values aren't supported for filters.</p>"""
    max_results: NotRequired[
        "aws_sdk_application_discovery_service.types.describe_import_tasks_max_results.DescribeImportTasksMaxResults"
    ]
    """<p>The maximum number of results that you want this request to return, up to 100.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The token to request a specific page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTasksRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_application_discovery_service.types.describe_import_tasks_filter_list

        out["filters"] = (
            aws_sdk_application_discovery_service.types.describe_import_tasks_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImportTasksRequest:
    out: DescribeImportTasksRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_application_discovery_service.types.describe_import_tasks_filter_list

        out["filters"] = (
            aws_sdk_application_discovery_service.types.describe_import_tasks_filter_list.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
