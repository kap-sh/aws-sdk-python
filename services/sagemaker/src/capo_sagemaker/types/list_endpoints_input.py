"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEndpointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name_contains
    import capo_sagemaker.types.endpoint_sort_key
    import capo_sagemaker.types.endpoint_status
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.order_key
    import capo_sagemaker.types.pagination_token
    import capo_sagemaker.types.timestamp


class ListEndpointsInput(TypedDict, closed=True):
    sort_by: NotRequired["capo_sagemaker.types.endpoint_sort_key.EndpointSortKey"]
    """<p>Sorts the list of results. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.order_key.OrderKey"]
    """<p>The sort order for results. The default is <code>Descending</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.pagination_token.PaginationToken"]
    """<p>If the result of a <code>ListEndpoints</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of endpoints, use the token in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of endpoints to return in the response. This value defaults to 10.</p>"""
    name_contains: NotRequired[
        "capo_sagemaker.types.endpoint_name_contains.EndpointNameContains"
    ]
    """<p>A string in endpoint names. This filter returns only endpoints whose name contains the specified string.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only endpoints that were created before the specified time (timestamp).</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only endpoints with a creation time greater than or equal to the specified time (timestamp).</p>"""
    last_modified_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p> A filter that returns only endpoints that were modified before the specified timestamp. </p>"""
    last_modified_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p> A filter that returns only endpoints that were modified after the specified timestamp. </p>"""
    status_equals: NotRequired["capo_sagemaker.types.endpoint_status.EndpointStatus"]
    """<p> A filter that returns only endpoints with the specified status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsInput) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_sagemaker.types.endpoint_sort_key

        out["SortBy"] = capo_sagemaker.types.endpoint_sort_key.serialize_aws_json_1_1(
            value["sort_by"]
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
    if "last_modified_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "status_equals" in value:
        import capo_sagemaker.types.endpoint_status

        out["StatusEquals"] = (
            capo_sagemaker.types.endpoint_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsInput:
    out: ListEndpointsInput = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import capo_sagemaker.types.endpoint_sort_key

        out["sort_by"] = (
            capo_sagemaker.types.endpoint_sort_key.deserialize_aws_json_1_1(
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
    if "LastModifiedTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "StatusEquals" in data:
        import capo_sagemaker.types.endpoint_status

        out["status_equals"] = (
            capo_sagemaker.types.endpoint_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    return out
