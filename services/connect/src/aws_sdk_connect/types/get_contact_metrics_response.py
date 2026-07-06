"""Generated from Smithy shape ``com.amazonaws.connect#GetContactMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_metric_results


class GetContactMetricsResponse(TypedDict, closed=True):
    metric_results: NotRequired[
        "aws_sdk_connect.types.contact_metric_results.ContactMetricResults"
    ]
    """<p>A list of metric results containing the calculated values for each requested metric. Each result includes the metric name and its corresponding value. For example, POSITION_IN_QUEUE returns a numeric value representing the contact's position in queue, and ESTIMATED_WAIT_TIME returns the predicted wait time in seconds.</p>"""
    id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The unique identifier of the contact for which metrics were retrieved. This matches the ContactId provided in the request.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The ARN of the contact for which metrics were retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactMetricsResponse) -> dict:
    out: dict = {}
    if "metric_results" in value:
        import aws_sdk_connect.types.contact_metric_results

        out["MetricResults"] = (
            aws_sdk_connect.types.contact_metric_results.serialize_json(
                value["metric_results"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetContactMetricsResponse:
    out: GetContactMetricsResponse = {}  # type: ignore[typeddict-item]
    if "MetricResults" in data:
        import aws_sdk_connect.types.contact_metric_results

        out["metric_results"] = (
            aws_sdk_connect.types.contact_metric_results.deserialize_json(
                data["MetricResults"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
