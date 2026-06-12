"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetAnomaliesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly_date_interval
    import aws_sdk_cost_explorer.types.anomaly_feedback_type
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.page_size
    import aws_sdk_cost_explorer.types.total_impact_filter


class GetAnomaliesRequest(TypedDict):
    monitor_arn: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>Retrieves all of the cost anomalies detected for a specific cost anomaly monitor Amazon Resource Name (ARN). </p>"""
    date_interval: (
        "aws_sdk_cost_explorer.types.anomaly_date_interval.AnomalyDateInterval"
    )
    """<p>Assigns the start and end dates for retrieving cost anomalies. The returned anomaly object will have an <code>AnomalyEndDate</code> in the specified time range. </p>"""
    feedback: NotRequired[
        "aws_sdk_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType"
    ]
    """<p>Filters anomaly results by the feedback field on the anomaly object. </p>"""
    total_impact: NotRequired[
        "aws_sdk_cost_explorer.types.total_impact_filter.TotalImpactFilter"
    ]
    """<p>Filters anomaly results by the total impact field on the anomaly object. For example, you can filter anomalies <code>GREATER_THAN 200.00</code> to retrieve anomalies, with an estimated dollar impact greater than 200. </p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""
    max_results: NotRequired["aws_sdk_cost_explorer.types.page_size.PageSize"]
    """<p>The number of entries a paginated response contains. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAnomaliesRequest) -> dict:
    out: dict = {}
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    import aws_sdk_cost_explorer.types.anomaly_date_interval

    out["DateInterval"] = (
        aws_sdk_cost_explorer.types.anomaly_date_interval.serialize_aws_json_1_1(
            value["date_interval"]
        )
    )
    if "feedback" in value:
        import aws_sdk_cost_explorer.types.anomaly_feedback_type

        out["Feedback"] = (
            aws_sdk_cost_explorer.types.anomaly_feedback_type.serialize_aws_json_1_1(
                value["feedback"]
            )
        )
    if "total_impact" in value:
        import aws_sdk_cost_explorer.types.total_impact_filter

        out["TotalImpact"] = (
            aws_sdk_cost_explorer.types.total_impact_filter.serialize_aws_json_1_1(
                value["total_impact"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAnomaliesRequest:
    out: GetAnomaliesRequest = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    if "DateInterval" in data:
        import aws_sdk_cost_explorer.types.anomaly_date_interval

        out["date_interval"] = (
            aws_sdk_cost_explorer.types.anomaly_date_interval.deserialize_aws_json_1_1(
                data["DateInterval"]
            )
        )
    else:
        raise DeserializationError("GetAnomaliesRequest.date_interval required")
    if "Feedback" in data:
        import aws_sdk_cost_explorer.types.anomaly_feedback_type

        out["feedback"] = (
            aws_sdk_cost_explorer.types.anomaly_feedback_type.deserialize_aws_json_1_1(
                data["Feedback"]
            )
        )
    if "TotalImpact" in data:
        import aws_sdk_cost_explorer.types.total_impact_filter

        out["total_impact"] = (
            aws_sdk_cost_explorer.types.total_impact_filter.deserialize_aws_json_1_1(
                data["TotalImpact"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
