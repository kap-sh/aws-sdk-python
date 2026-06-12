"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingJobsForHyperParameterTuningJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.training_job_sort_by_options
    import aws_sdk_sagemaker.types.training_job_status


class ListTrainingJobsForHyperParameterTuningJobRequest(TypedDict):
    hyper_parameter_tuning_job_name: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The name of the tuning job whose training jobs you want to list.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListTrainingJobsForHyperParameterTuningJob</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of training jobs, use the token in the next request.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of training jobs to return. The default value is 10.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status.TrainingJobStatus"
    ]
    """<p>A filter that returns only training jobs with the specified status.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.training_job_sort_by_options.TrainingJobSortByOptions"
    ]
    """<p>The field to sort results by. The default is <code>Name</code>.</p> <p>If the value of this field is <code>FinalObjectiveMetricValue</code>, any training jobs that did not return an objective metric are not listed.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListTrainingJobsForHyperParameterTuningJobRequest,
) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_name" in value:
        out["HyperParameterTuningJobName"] = value["hyper_parameter_tuning_job_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.training_job_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.training_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.training_job_sort_by_options

        out["SortBy"] = (
            aws_sdk_sagemaker.types.training_job_sort_by_options.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListTrainingJobsForHyperParameterTuningJobRequest:
    out: ListTrainingJobsForHyperParameterTuningJobRequest = {}  # type: ignore[typeddict-item]
    if "HyperParameterTuningJobName" in data:
        out["hyper_parameter_tuning_job_name"] = data["HyperParameterTuningJobName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.training_job_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.training_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.training_job_sort_by_options

        out["sort_by"] = (
            aws_sdk_sagemaker.types.training_job_sort_by_options.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
