"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorMonitorEvaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.evaluation_state
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.metric_results
    import aws_sdk_forecast.types.monitor_data_source
    import aws_sdk_forecast.types.predictor_event
    import aws_sdk_forecast.types.timestamp


class PredictorMonitorEvaluation(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource to monitor.</p>"""
    monitor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the monitor resource.</p>"""
    evaluation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates when the monitor evaluation was started. </p>"""
    evaluation_state: NotRequired[
        "aws_sdk_forecast.types.evaluation_state.EvaluationState"
    ]
    """<p>The status of the monitor evaluation. The state can be <code>SUCCESS</code> or <code>FAILURE</code>.</p>"""
    window_start_datetime: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates the start of the window that is used for monitor evaluation.</p>"""
    window_end_datetime: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates the end of the window that is used for monitor evaluation.</p>"""
    predictor_event: NotRequired[
        "aws_sdk_forecast.types.predictor_event.PredictorEvent"
    ]
    """<p>Provides details about a predictor event, such as a retraining.</p>"""
    monitor_data_source: NotRequired[
        "aws_sdk_forecast.types.monitor_data_source.MonitorDataSource"
    ]
    """<p>The source of the data the monitor resource used during the evaluation.</p>"""
    metric_results: NotRequired["aws_sdk_forecast.types.metric_results.MetricResults"]
    """<p>A list of metrics Forecast calculated when monitoring a predictor. You can compare the value for each metric in the list to the metric's value in the <a>Baseline</a> to see how your predictor's performance is changing.</p>"""
    num_items_evaluated: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The number of items considered during the evaluation.</p>"""
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>Information about any errors that may have occurred during the monitor evaluation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorMonitorEvaluation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    if "evaluation_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["EvaluationTime"] = aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
            value["evaluation_time"]
        )
    if "evaluation_state" in value:
        out["EvaluationState"] = value["evaluation_state"]
    if "window_start_datetime" in value:
        import aws_sdk_forecast.types.timestamp

        out["WindowStartDatetime"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["window_start_datetime"]
            )
        )
    if "window_end_datetime" in value:
        import aws_sdk_forecast.types.timestamp

        out["WindowEndDatetime"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["window_end_datetime"]
            )
        )
    if "predictor_event" in value:
        import aws_sdk_forecast.types.predictor_event

        out["PredictorEvent"] = (
            aws_sdk_forecast.types.predictor_event.serialize_aws_json_1_1(
                value["predictor_event"]
            )
        )
    if "monitor_data_source" in value:
        import aws_sdk_forecast.types.monitor_data_source

        out["MonitorDataSource"] = (
            aws_sdk_forecast.types.monitor_data_source.serialize_aws_json_1_1(
                value["monitor_data_source"]
            )
        )
    if "metric_results" in value:
        import aws_sdk_forecast.types.metric_results

        out["MetricResults"] = (
            aws_sdk_forecast.types.metric_results.serialize_aws_json_1_1(
                value["metric_results"]
            )
        )
    if "num_items_evaluated" in value:
        out["NumItemsEvaluated"] = value["num_items_evaluated"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorMonitorEvaluation:
    out: PredictorMonitorEvaluation = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    if "EvaluationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["evaluation_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["EvaluationTime"]
            )
        )
    if "EvaluationState" in data:
        out["evaluation_state"] = data["EvaluationState"]
    if "WindowStartDatetime" in data:
        import aws_sdk_forecast.types.timestamp

        out["window_start_datetime"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["WindowStartDatetime"]
            )
        )
    if "WindowEndDatetime" in data:
        import aws_sdk_forecast.types.timestamp

        out["window_end_datetime"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["WindowEndDatetime"]
            )
        )
    if "PredictorEvent" in data:
        import aws_sdk_forecast.types.predictor_event

        out["predictor_event"] = (
            aws_sdk_forecast.types.predictor_event.deserialize_aws_json_1_1(
                data["PredictorEvent"]
            )
        )
    if "MonitorDataSource" in data:
        import aws_sdk_forecast.types.monitor_data_source

        out["monitor_data_source"] = (
            aws_sdk_forecast.types.monitor_data_source.deserialize_aws_json_1_1(
                data["MonitorDataSource"]
            )
        )
    if "MetricResults" in data:
        import aws_sdk_forecast.types.metric_results

        out["metric_results"] = (
            aws_sdk_forecast.types.metric_results.deserialize_aws_json_1_1(
                data["MetricResults"]
            )
        )
    if "NumItemsEvaluated" in data:
        out["num_items_evaluated"] = data["NumItemsEvaluated"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
