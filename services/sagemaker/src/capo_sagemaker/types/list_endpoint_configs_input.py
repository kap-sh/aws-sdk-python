"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEndpointConfigsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_config_name_contains
    import capo_sagemaker.types.endpoint_config_sort_key
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.order_key
    import capo_sagemaker.types.pagination_token
    import capo_sagemaker.types.timestamp


class ListEndpointConfigsInput(TypedDict, closed=True):
    sort_by: NotRequired[
        "capo_sagemaker.types.endpoint_config_sort_key.EndpointConfigSortKey"
    ]
    """<p>The field to sort results by. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.order_key.OrderKey"]
    """<p>The sort order for results. The default is <code>Descending</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.pagination_token.PaginationToken"]
    """<p>If the result of the previous <code>ListEndpointConfig</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of endpoint configurations, use the token in the next request. </p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of training jobs to return in the response.</p>"""
    name_contains: NotRequired[
        "capo_sagemaker.types.endpoint_config_name_contains.EndpointConfigNameContains"
    ]
    """<p>A string in the endpoint configuration name. This filter returns only endpoint configurations whose name contains the specified string. </p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only endpoint configurations created before the specified time (timestamp).</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only endpoint configurations with a creation time greater than or equal to the specified time (timestamp).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointConfigsInput) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_sagemaker.types.endpoint_config_sort_key

        out["SortBy"] = (
            capo_sagemaker.types.endpoint_config_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.order_key

        out["SortOrder"] = capo_sagemaker.types.order_key.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointConfigsInput:
    out: ListEndpointConfigsInput = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import capo_sagemaker.types.endpoint_config_sort_key

        out["sort_by"] = (
            capo_sagemaker.types.endpoint_config_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.order_key

        out["sort_order"] = capo_sagemaker.types.order_key.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    return out
