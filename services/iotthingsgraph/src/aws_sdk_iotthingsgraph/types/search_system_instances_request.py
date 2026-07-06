"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchSystemInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.max_results
    import aws_sdk_iotthingsgraph.types.next_token
    import aws_sdk_iotthingsgraph.types.system_instance_filters


class SearchSystemInstancesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_instance_filters.SystemInstanceFilters"
    ]
    """<p>Optional filter to apply to the search. Valid filters are <code>SYSTEM_TEMPLATE_ID</code>, <code>STATUS</code>, and <code>GREENGRASS_GROUP_NAME</code>.</p> <p>Multiple filters function as OR criteria in the query. Multiple values passed inside the filter function as AND criteria.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["aws_sdk_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSystemInstancesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_iotthingsgraph.types.system_instance_filters

        out["filters"] = (
            aws_sdk_iotthingsgraph.types.system_instance_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchSystemInstancesRequest:
    out: SearchSystemInstancesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_filters

        out["filters"] = (
            aws_sdk_iotthingsgraph.types.system_instance_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
