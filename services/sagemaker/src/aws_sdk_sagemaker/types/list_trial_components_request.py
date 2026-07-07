"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrialComponentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.sort_trial_components_by
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp


class ListTrialComponentsRequest(TypedDict, closed=True):
    experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>A filter that returns only components that are part of the specified experiment. If you specify <code>ExperimentName</code>, you can't filter by <code>SourceArn</code> or <code>TrialName</code>.</p>"""
    trial_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>A filter that returns only components that are part of the specified trial. If you specify <code>TrialName</code>, you can't filter by <code>ExperimentName</code> or <code>SourceArn</code>.</p>"""
    source_arn: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>A filter that returns only components that have the specified source Amazon Resource Name (ARN). If you specify <code>SourceArn</code>, you can't filter by <code>ExperimentName</code> or <code>TrialName</code>.</p>"""
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only components created after the specified time.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only components created before the specified time.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.sort_trial_components_by.SortTrialComponentsBy"
    ]
    """<p>The property used to sort results. The default value is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order. The default value is <code>Descending</code>.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of components to return in the response. The default value is 10.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to <code>ListTrialComponents</code> didn't return the full set of components, the call returns a token for getting the next set of components.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrialComponentsRequest) -> dict:
    out: dict = {}
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_trial_components_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_trial_components_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrialComponentsRequest:
    out: ListTrialComponentsRequest = {}  # type: ignore[typeddict-item]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_trial_components_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_trial_components_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
