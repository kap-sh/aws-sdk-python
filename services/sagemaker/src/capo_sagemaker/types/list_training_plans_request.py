"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingPlansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_plan_filters
    import capo_sagemaker.types.training_plan_sort_by
    import capo_sagemaker.types.training_plan_sort_order


class ListTrainingPlansRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to continue pagination if more results are available.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    start_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter to list only training plans with an actual start time after this date.</p>"""
    start_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter to list only training plans with an actual start time before this date.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.training_plan_sort_by.TrainingPlanSortBy"
    ]
    """<p>The training plan field to sort the results by (e.g., StartTime, Status).</p>"""
    sort_order: NotRequired[
        "capo_sagemaker.types.training_plan_sort_order.TrainingPlanSortOrder"
    ]
    """<p>The order to sort the results (Ascending or Descending).</p>"""
    filters: NotRequired[
        "capo_sagemaker.types.training_plan_filters.TrainingPlanFilters"
    ]
    """<p>Additional filters to apply to the list of training plans.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingPlansRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "start_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["StartTimeAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time_after"]
        )
    if "start_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["StartTimeBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time_before"]
        )
    if "sort_by" in value:
        import capo_sagemaker.types.training_plan_sort_by

        out["SortBy"] = (
            capo_sagemaker.types.training_plan_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.training_plan_sort_order

        out["SortOrder"] = (
            capo_sagemaker.types.training_plan_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "filters" in value:
        import capo_sagemaker.types.training_plan_filters

        out["Filters"] = (
            capo_sagemaker.types.training_plan_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingPlansRequest:
    out: ListTrainingPlansRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "StartTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["start_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["StartTimeAfter"]
            )
        )
    if "StartTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["start_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["StartTimeBefore"]
            )
        )
    if "SortBy" in data:
        import capo_sagemaker.types.training_plan_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.training_plan_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.training_plan_sort_order

        out["sort_order"] = (
            capo_sagemaker.types.training_plan_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "Filters" in data:
        import capo_sagemaker.types.training_plan_filters

        out["filters"] = (
            capo_sagemaker.types.training_plan_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
