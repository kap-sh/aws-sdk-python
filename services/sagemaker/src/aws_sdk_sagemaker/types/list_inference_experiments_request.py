"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceExperimentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_experiment_status
    import aws_sdk_sagemaker.types.inference_experiment_type
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_inference_experiments_by
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListInferenceExperimentsRequest(TypedDict):
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>Selects inference experiments whose names contain this name.</p>"""
    type: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_type.InferenceExperimentType"
    ]
    r"""<p> Selects inference experiments of this type. For the possible types of inference experiments, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html\">CreateInferenceExperiment</a>. </p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_status.InferenceExperimentStatus"
    ]
    r"""<p> Selects inference experiments which are in this status. For the possible statuses, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html\">DescribeInferenceExperiment</a>. </p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects inference experiments which were created after this timestamp.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects inference experiments which were created before this timestamp.</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects inference experiments which were last modified after this timestamp.</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>Selects inference experiments which were last modified before this timestamp.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.sort_inference_experiments_by.SortInferenceExperimentsBy"
    ]
    """<p>The column by which to sort the listed inference experiments.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The direction of sorting (ascending or descending).</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p> The response from the last list when returning a list large enough to need tokening. </p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to select.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceExperimentsRequest) -> dict:
    out: dict = {}
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "type" in value:
        import aws_sdk_sagemaker.types.inference_experiment_type

        out["Type"] = (
            aws_sdk_sagemaker.types.inference_experiment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.inference_experiment_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.inference_experiment_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
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
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_inference_experiments_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_inference_experiments_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceExperimentsRequest:
    out: ListInferenceExperimentsRequest = {}  # type: ignore[typeddict-item]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "Type" in data:
        import aws_sdk_sagemaker.types.inference_experiment_type

        out["type"] = (
            aws_sdk_sagemaker.types.inference_experiment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.inference_experiment_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.inference_experiment_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
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
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_inference_experiments_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_inference_experiments_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
