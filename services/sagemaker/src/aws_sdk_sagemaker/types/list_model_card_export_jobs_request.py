"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelCardExportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.model_card_export_job_sort_by
    import aws_sdk_sagemaker.types.model_card_export_job_sort_order
    import aws_sdk_sagemaker.types.model_card_export_job_status
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.timestamp


class ListModelCardExportJobsRequest(TypedDict, closed=True):
    model_card_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>List export jobs for the model card with the specified name.</p>"""
    model_card_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>List export jobs for the model card with the specified version.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list model card export jobs that were created after the time specified.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list model card export jobs that were created before the time specified.</p>"""
    model_card_export_job_name_contains: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>Only list model card export jobs with names that contain the specified string.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_status.ModelCardExportJobStatus"
    ]
    """<p>Only list model card export jobs with the specified status.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_sort_by.ModelCardExportJobSortBy"
    ]
    """<p>Sort model card export jobs by either name or creation time. Sorts by creation time by default.</p>"""
    sort_order: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_sort_order.ModelCardExportJobSortOrder"
    ]
    """<p>Sort model card export jobs by ascending or descending order.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response to a previous <code>ListModelCardExportJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of model card export jobs, use the token in the next request.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of model card export jobs to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelCardExportJobsRequest) -> dict:
    out: dict = {}
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
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
    if "model_card_export_job_name_contains" in value:
        out["ModelCardExportJobNameContains"] = value[
            "model_card_export_job_name_contains"
        ]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.model_card_export_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.model_card_export_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.model_card_export_job_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.model_card_export_job_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.model_card_export_job_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.model_card_export_job_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelCardExportJobsRequest:
    out: ListModelCardExportJobsRequest = {}  # type: ignore[typeddict-item]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardVersion" in data:
        out["model_card_version"] = data["ModelCardVersion"]
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
    if "ModelCardExportJobNameContains" in data:
        out["model_card_export_job_name_contains"] = data[
            "ModelCardExportJobNameContains"
        ]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.model_card_export_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.model_card_export_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.model_card_export_job_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.model_card_export_job_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.model_card_export_job_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.model_card_export_job_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
