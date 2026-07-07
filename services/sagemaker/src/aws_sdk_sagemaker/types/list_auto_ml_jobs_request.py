"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAutoMLJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_status
    import aws_sdk_sagemaker.types.auto_ml_max_results
    import aws_sdk_sagemaker.types.auto_ml_name_contains
    import aws_sdk_sagemaker.types.auto_ml_sort_by
    import aws_sdk_sagemaker.types.auto_ml_sort_order
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.timestamp


class ListAutoMLJobsRequest(TypedDict, closed=True):
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Request a list of jobs, using a filter for time.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Request a list of jobs, using a filter for time.</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Request a list of jobs, using a filter for time.</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>Request a list of jobs, using a filter for time.</p>"""
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_name_contains.AutoMLNameContains"
    ]
    """<p>Request a list of jobs, using a search filter for name.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_status.AutoMLJobStatus"
    ]
    """<p>Request a list of jobs, using a filter for status.</p>"""
    sort_order: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_sort_order.AutoMLSortOrder"
    ]
    """<p>The sort order for the results. The default is <code>Descending</code>.</p>"""
    sort_by: NotRequired["aws_sdk_sagemaker.types.auto_ml_sort_by.AutoMLSortBy"]
    """<p>The parameter by which to sort the results. The default is <code>Name</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_max_results.AutoMLMaxResults"
    ]
    """<p>Request a list of jobs up to a specified limit.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAutoMLJobsRequest) -> dict:
    out: dict = {}
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.auto_ml_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.auto_ml_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.auto_ml_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.auto_ml_sort_by

        out["SortBy"] = aws_sdk_sagemaker.types.auto_ml_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAutoMLJobsRequest:
    out: ListAutoMLJobsRequest = {}  # type: ignore[typeddict-item]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.auto_ml_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.auto_ml_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.auto_ml_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.auto_ml_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.auto_ml_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
