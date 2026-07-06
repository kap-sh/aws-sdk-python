"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgePackagingJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_packaging_job_status
    import aws_sdk_sagemaker.types.list_edge_packaging_jobs_sort_by
    import aws_sdk_sagemaker.types.list_max_results
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListEdgePackagingJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to need tokening.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.list_max_results.ListMaxResults"]
    """<p>Maximum number of results to select.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Select jobs where the job was created after specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Select jobs where the job was created before specified time.</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Select jobs where the job was updated after specified time.</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>Select jobs where the job was updated before specified time.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>Filter for jobs containing this name in their packaging job name.</p>"""
    model_name_contains: NotRequired[
        "aws_sdk_sagemaker.types.name_contains.NameContains"
    ]
    """<p>Filter for jobs where the model name contains this string.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.edge_packaging_job_status.EdgePackagingJobStatus"
    ]
    """<p>The job status to filter for.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.list_edge_packaging_jobs_sort_by.ListEdgePackagingJobsSortBy"
    ]
    """<p>Use to specify what column to sort by.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>What direction to sort by.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEdgePackagingJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
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
    if "model_name_contains" in value:
        out["ModelNameContains"] = value["model_name_contains"]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.edge_packaging_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.edge_packaging_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.list_edge_packaging_jobs_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.list_edge_packaging_jobs_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEdgePackagingJobsRequest:
    out: ListEdgePackagingJobsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
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
    if "ModelNameContains" in data:
        out["model_name_contains"] = data["ModelNameContains"]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.edge_packaging_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.edge_packaging_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.list_edge_packaging_jobs_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.list_edge_packaging_jobs_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
