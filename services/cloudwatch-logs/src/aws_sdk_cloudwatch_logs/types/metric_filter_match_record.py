"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricFilterMatchRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.event_message
    import aws_sdk_cloudwatch_logs.types.event_number
    import aws_sdk_cloudwatch_logs.types.extracted_values


class MetricFilterMatchRecord(TypedDict, closed=True):
    event_number: "aws_sdk_cloudwatch_logs.types.event_number.EventNumber"
    """<p>The event number.</p>"""
    event_message: NotRequired[
        "aws_sdk_cloudwatch_logs.types.event_message.EventMessage"
    ]
    """<p>The raw event data.</p>"""
    extracted_values: NotRequired[
        "aws_sdk_cloudwatch_logs.types.extracted_values.ExtractedValues"
    ]
    """<p>The values extracted from the event data by the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricFilterMatchRecord) -> dict:
    out: dict = {}
    out["eventNumber"] = value.get("event_number", 0)
    if "event_message" in value:
        out["eventMessage"] = value["event_message"]
    if "extracted_values" in value:
        import aws_sdk_cloudwatch_logs.types.extracted_values

        out["extractedValues"] = (
            aws_sdk_cloudwatch_logs.types.extracted_values.serialize_aws_json_1_1(
                value["extracted_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricFilterMatchRecord:
    out: MetricFilterMatchRecord = {}  # type: ignore[typeddict-item]
    if "eventNumber" in data:
        out["event_number"] = data["eventNumber"]
    else:
        out["event_number"] = 0
    if "eventMessage" in data:
        out["event_message"] = data["eventMessage"]
    if "extractedValues" in data:
        import aws_sdk_cloudwatch_logs.types.extracted_values

        out["extracted_values"] = (
            aws_sdk_cloudwatch_logs.types.extracted_values.deserialize_aws_json_1_1(
                data["extractedValues"]
            )
        )
    return out
