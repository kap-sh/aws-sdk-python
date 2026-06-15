"""Generated from Smithy shape ``com.amazonaws.forecast#ListMonitorEvaluationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.next_token
    import aws_sdk_forecast.types.predictor_monitor_evaluations


class ListMonitorEvaluationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>"""
    predictor_monitor_evaluations: NotRequired[
        "aws_sdk_forecast.types.predictor_monitor_evaluations.PredictorMonitorEvaluations"
    ]
    r"""<p>The monitoring results and predictor events collected by the monitor resource during different windows of time.</p> <p>For information about monitoring see <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html\">Viewing Monitoring Results</a>. For more information about retrieving monitoring results see <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html\">Viewing Monitoring Results</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitorEvaluationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "predictor_monitor_evaluations" in value:
        import aws_sdk_forecast.types.predictor_monitor_evaluations

        out["PredictorMonitorEvaluations"] = (
            aws_sdk_forecast.types.predictor_monitor_evaluations.serialize_aws_json_1_1(
                value["predictor_monitor_evaluations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitorEvaluationsResponse:
    out: ListMonitorEvaluationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PredictorMonitorEvaluations" in data:
        import aws_sdk_forecast.types.predictor_monitor_evaluations

        out["predictor_monitor_evaluations"] = (
            aws_sdk_forecast.types.predictor_monitor_evaluations.deserialize_aws_json_1_1(
                data["PredictorMonitorEvaluations"]
            )
        )
    return out
