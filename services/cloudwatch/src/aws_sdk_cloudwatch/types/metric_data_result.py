"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDataResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.datapoint_values
    import aws_sdk_cloudwatch.types.metric_data_result_messages
    import aws_sdk_cloudwatch.types.metric_id
    import aws_sdk_cloudwatch.types.metric_label
    import aws_sdk_cloudwatch.types.status_code
    import aws_sdk_cloudwatch.types.timestamps


class MetricDataResult(TypedDict):
    id: NotRequired["aws_sdk_cloudwatch.types.metric_id.MetricId"]
    """<p>The short name you specified to represent this metric.</p>"""
    label: NotRequired["aws_sdk_cloudwatch.types.metric_label.MetricLabel"]
    """<p>The human-readable label associated with the data.</p>"""
    timestamps: NotRequired["aws_sdk_cloudwatch.types.timestamps.Timestamps"]
    """<p>The timestamps for the data points, formatted in Unix timestamp format. The number of timestamps always matches the number of values and the value for Timestamps[x] is Values[x].</p>"""
    values: NotRequired["aws_sdk_cloudwatch.types.datapoint_values.DatapointValues"]
    """<p>The data points for the metric corresponding to <code>Timestamps</code>. The number of values always matches the number of timestamps and the timestamp for Values[x] is Timestamps[x].</p>"""
    status_code: NotRequired["aws_sdk_cloudwatch.types.status_code.StatusCode"]
    """<p>The status of the returned data. <code>Complete</code> indicates that all data points in the requested time range were returned. <code>PartialData</code> means that an incomplete set of data points were returned. You can use the <code>NextToken</code> value that was returned and repeat your request to get more data points. <code>NextToken</code> is not returned if you are performing a math expression. <code>InternalError</code> indicates that an error occurred. Retry your request using <code>NextToken</code>, if present.</p>"""
    messages: NotRequired[
        "aws_sdk_cloudwatch.types.metric_data_result_messages.MetricDataResultMessages"
    ]
    """<p>A list of messages with additional information about the data returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDataResult) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "label" in value:
        out["Label"] = value["label"]
    if "timestamps" in value:
        import aws_sdk_cloudwatch.types.timestamps

        out["Timestamps"] = aws_sdk_cloudwatch.types.timestamps.serialize_aws_json_1_0(
            value["timestamps"]
        )
    if "values" in value:
        import aws_sdk_cloudwatch.types.datapoint_values

        out["Values"] = (
            aws_sdk_cloudwatch.types.datapoint_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    if "status_code" in value:
        import aws_sdk_cloudwatch.types.status_code

        out["StatusCode"] = aws_sdk_cloudwatch.types.status_code.serialize_aws_json_1_0(
            value["status_code"]
        )
    if "messages" in value:
        import aws_sdk_cloudwatch.types.metric_data_result_messages

        out["Messages"] = (
            aws_sdk_cloudwatch.types.metric_data_result_messages.serialize_aws_json_1_0(
                value["messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricDataResult:
    out: MetricDataResult = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Label" in data:
        out["label"] = data["Label"]
    if "Timestamps" in data:
        import aws_sdk_cloudwatch.types.timestamps

        out["timestamps"] = (
            aws_sdk_cloudwatch.types.timestamps.deserialize_aws_json_1_0(
                data["Timestamps"]
            )
        )
    if "Values" in data:
        import aws_sdk_cloudwatch.types.datapoint_values

        out["values"] = (
            aws_sdk_cloudwatch.types.datapoint_values.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    if "StatusCode" in data:
        import aws_sdk_cloudwatch.types.status_code

        out["status_code"] = (
            aws_sdk_cloudwatch.types.status_code.deserialize_aws_json_1_0(
                data["StatusCode"]
            )
        )
    if "Messages" in data:
        import aws_sdk_cloudwatch.types.metric_data_result_messages

        out["messages"] = (
            aws_sdk_cloudwatch.types.metric_data_result_messages.deserialize_aws_json_1_0(
                data["Messages"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "label" in value:
        pairs.append((f"{prefix}.Label", str(value["label"])))
    if "timestamps" in value:
        import aws_sdk_cloudwatch.types.timestamps

        aws_sdk_cloudwatch.types.timestamps.serialize_query(
            value["timestamps"], pairs, f"{prefix}.Timestamps"
        )
    if "values" in value:
        import aws_sdk_cloudwatch.types.datapoint_values

        aws_sdk_cloudwatch.types.datapoint_values.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )
    if "status_code" in value:
        import aws_sdk_cloudwatch.types.status_code

        aws_sdk_cloudwatch.types.status_code.serialize_query(
            value["status_code"], pairs, f"{prefix}.StatusCode"
        )
    if "messages" in value:
        import aws_sdk_cloudwatch.types.metric_data_result_messages

        aws_sdk_cloudwatch.types.metric_data_result_messages.serialize_query(
            value["messages"], pairs, f"{prefix}.Messages"
        )


def deserialize_query(el: Element) -> MetricDataResult:
    out: MetricDataResult = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    child_timestamps = el.find("Timestamps")
    if child_timestamps is not None:
        import aws_sdk_cloudwatch.types.timestamps

        out["timestamps"] = aws_sdk_cloudwatch.types.timestamps.deserialize_query(
            child_timestamps
        )
    child_values = el.find("Values")
    if child_values is not None:
        import aws_sdk_cloudwatch.types.datapoint_values

        out["values"] = aws_sdk_cloudwatch.types.datapoint_values.deserialize_query(
            child_values
        )
    child_status_code = el.find("StatusCode")
    if child_status_code is not None:
        import aws_sdk_cloudwatch.types.status_code

        out["status_code"] = aws_sdk_cloudwatch.types.status_code.deserialize_query(
            child_status_code
        )
    child_messages = el.find("Messages")
    if child_messages is not None:
        import aws_sdk_cloudwatch.types.metric_data_result_messages

        out["messages"] = (
            aws_sdk_cloudwatch.types.metric_data_result_messages.deserialize_query(
                child_messages
            )
        )
    return out
