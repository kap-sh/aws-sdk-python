"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogAnomalyClass``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.explanation
    import aws_sdk_devops_guru.types.log_anomaly_token
    import aws_sdk_devops_guru.types.log_anomaly_type
    import aws_sdk_devops_guru.types.log_event_id
    import aws_sdk_devops_guru.types.log_stream_name
    import aws_sdk_devops_guru.types.number_of_log_lines_occurrences
    import aws_sdk_devops_guru.types.timestamp


class LogAnomalyClass(TypedDict):
    log_stream_name: NotRequired[
        "aws_sdk_devops_guru.types.log_stream_name.LogStreamName"
    ]
    """<p> The name of the Amazon CloudWatch log stream that the anomalous log event belongs to. A log stream is a sequence of log events that share the same source. </p>"""
    log_anomaly_type: NotRequired[
        "aws_sdk_devops_guru.types.log_anomaly_type.LogAnomalyType"
    ]
    """<p> The type of log anomaly that has been detected. </p>"""
    log_anomaly_token: NotRequired[
        "aws_sdk_devops_guru.types.log_anomaly_token.LogAnomalyToken"
    ]
    """<p> The token where the anomaly was detected. This may refer to an exception or another location, or it may be blank for log anomalies such as format anomalies. </p>"""
    log_event_id: NotRequired["aws_sdk_devops_guru.types.log_event_id.LogEventId"]
    """<p> The ID of the log event. </p>"""
    explanation: NotRequired["aws_sdk_devops_guru.types.explanation.Explanation"]
    """<p> The explanation for why the log event is considered an anomaly. </p>"""
    number_of_log_lines_occurrences: "aws_sdk_devops_guru.types.number_of_log_lines_occurrences.NumberOfLogLinesOccurrences"
    """<p> The number of log lines where this anomalous log event occurs. </p>"""
    log_event_timestamp: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time of the first occurrence of the anomalous log event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogAnomalyClass) -> dict:
    out: dict = {}
    if "log_stream_name" in value:
        out["LogStreamName"] = value["log_stream_name"]
    if "log_anomaly_type" in value:
        import aws_sdk_devops_guru.types.log_anomaly_type

        out["LogAnomalyType"] = (
            aws_sdk_devops_guru.types.log_anomaly_type.serialize_json(
                value["log_anomaly_type"]
            )
        )
    if "log_anomaly_token" in value:
        out["LogAnomalyToken"] = value["log_anomaly_token"]
    if "log_event_id" in value:
        out["LogEventId"] = value["log_event_id"]
    if "explanation" in value:
        out["Explanation"] = value["explanation"]
    out["NumberOfLogLinesOccurrences"] = value.get("number_of_log_lines_occurrences", 0)
    if "log_event_timestamp" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["LogEventTimestamp"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["log_event_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> LogAnomalyClass:
    out: LogAnomalyClass = {}  # type: ignore[typeddict-item]
    if "LogStreamName" in data:
        out["log_stream_name"] = data["LogStreamName"]
    if "LogAnomalyType" in data:
        import aws_sdk_devops_guru.types.log_anomaly_type

        out["log_anomaly_type"] = (
            aws_sdk_devops_guru.types.log_anomaly_type.deserialize_json(
                data["LogAnomalyType"]
            )
        )
    if "LogAnomalyToken" in data:
        out["log_anomaly_token"] = data["LogAnomalyToken"]
    if "LogEventId" in data:
        out["log_event_id"] = data["LogEventId"]
    if "Explanation" in data:
        out["explanation"] = data["Explanation"]
    if "NumberOfLogLinesOccurrences" in data:
        out["number_of_log_lines_occurrences"] = data["NumberOfLogLinesOccurrences"]
    else:
        out["number_of_log_lines_occurrences"] = 0
    if "LogEventTimestamp" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["log_event_timestamp"] = (
            aws_sdk_devops_guru.types.timestamp.deserialize_json(
                data["LogEventTimestamp"]
            )
        )
    return out
