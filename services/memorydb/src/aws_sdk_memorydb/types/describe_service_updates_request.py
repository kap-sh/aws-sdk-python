"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeServiceUpdatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.cluster_name_list
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.service_update_status_list
    import aws_sdk_memorydb.types.string


class DescribeServiceUpdatesRequest(TypedDict, closed=True):
    service_update_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The unique ID of the service update to describe.</p>"""
    cluster_names: NotRequired[
        "aws_sdk_memorydb.types.cluster_name_list.ClusterNameList"
    ]
    """<p>The list of cluster names to identify service updates to apply.</p>"""
    status: NotRequired[
        "aws_sdk_memorydb.types.service_update_status_list.ServiceUpdateStatusList"
    ]
    """<p>The status(es) of the service updates to filter on.</p>"""
    max_results: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceUpdatesRequest) -> dict:
    out: dict = {}
    if "service_update_name" in value:
        out["ServiceUpdateName"] = value["service_update_name"]
    if "cluster_names" in value:
        import aws_sdk_memorydb.types.cluster_name_list

        out["ClusterNames"] = (
            aws_sdk_memorydb.types.cluster_name_list.serialize_aws_json_1_1(
                value["cluster_names"]
            )
        )
    if "status" in value:
        import aws_sdk_memorydb.types.service_update_status_list

        out["Status"] = (
            aws_sdk_memorydb.types.service_update_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceUpdatesRequest:
    out: DescribeServiceUpdatesRequest = {}  # type: ignore[typeddict-item]
    if "ServiceUpdateName" in data:
        out["service_update_name"] = data["ServiceUpdateName"]
    if "ClusterNames" in data:
        import aws_sdk_memorydb.types.cluster_name_list

        out["cluster_names"] = (
            aws_sdk_memorydb.types.cluster_name_list.deserialize_aws_json_1_1(
                data["ClusterNames"]
            )
        )
    if "Status" in data:
        import aws_sdk_memorydb.types.service_update_status_list

        out["status"] = (
            aws_sdk_memorydb.types.service_update_status_list.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
