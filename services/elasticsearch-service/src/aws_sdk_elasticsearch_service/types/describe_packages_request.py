"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.describe_packages_filter_list
    import aws_sdk_elasticsearch_service.types.max_results
    import aws_sdk_elasticsearch_service.types.next_token


class DescribePackagesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_elasticsearch_service.types.describe_packages_filter_list.DescribePackagesFilterList"
    ]
    """<p>Only returns packages that match the <code>DescribePackagesFilterList</code> values.</p>"""
    max_results: "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
    """<p>Limits results to a maximum number of packages.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_elasticsearch_service.types.describe_packages_filter_list

        out["Filters"] = (
            aws_sdk_elasticsearch_service.types.describe_packages_filter_list.serialize_json(
                value["filters"]
            )
        )
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribePackagesRequest:
    out: DescribePackagesRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_elasticsearch_service.types.describe_packages_filter_list

        out["filters"] = (
            aws_sdk_elasticsearch_service.types.describe_packages_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
