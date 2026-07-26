"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelBiasJobDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.monitoring_job_definition_sort_key
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListModelBiasJobDefinitionsRequest(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>Name of the endpoint to monitor for model bias.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_sort_key.MonitoringJobDefinitionSortKey"
    ]
    """<p>Whether to sort results by the <code>Name</code> or <code>CreationTime</code> field. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>Whether to sort the results in <code>Ascending</code> or <code>Descending</code> order. The default is <code>Descending</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of model bias jobs to return in the response. The default value is 10.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>Filter for model bias jobs whose name contains a specified string.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only model bias jobs created before a specified time.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only model bias jobs created after a specified time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelBiasJobDefinitionsRequest) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "sort_by" in value:
        import capo_sagemaker.types.monitoring_job_definition_sort_key

        out["SortBy"] = (
            capo_sagemaker.types.monitoring_job_definition_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> ListModelBiasJobDefinitionsRequest:
    out: ListModelBiasJobDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "SortBy" in data:
        import capo_sagemaker.types.monitoring_job_definition_sort_key

        out["sort_by"] = (
            capo_sagemaker.types.monitoring_job_definition_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
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
