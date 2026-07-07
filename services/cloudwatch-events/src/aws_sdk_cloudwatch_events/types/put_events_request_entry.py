"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutEventsRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.event_resource_list
    import aws_sdk_cloudwatch_events.types.event_time
    import aws_sdk_cloudwatch_events.types.non_partner_event_bus_name_or_arn
    import aws_sdk_cloudwatch_events.types.string
    import aws_sdk_cloudwatch_events.types.trace_header


class PutEventsRequestEntry(TypedDict, closed=True):
    time: NotRequired["aws_sdk_cloudwatch_events.types.event_time.EventTime"]
    r"""<p>The time stamp of the event, per <a href=\"https://www.rfc-editor.org/rfc/rfc3339.txt\">RFC3339</a>. If no time stamp is provided, the time stamp of the <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html\">PutEvents</a> call is used.</p>"""
    source: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The source of the event.</p>"""
    resources: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_resource_list.EventResourceList"
    ]
    """<p>Amazon Web Services resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.</p>"""
    detail_type: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>Free-form string used to decide what fields to expect in the event detail.</p>"""
    detail: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects.</p>"""
    event_bus_name: NotRequired[
        "aws_sdk_cloudwatch_events.types.non_partner_event_bus_name_or_arn.NonPartnerEventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus to receive the event. Only the rules that are associated with this event bus are used to match the event. If you omit this, the default event bus is used.</p>"""
    trace_header: NotRequired[
        "aws_sdk_cloudwatch_events.types.trace_header.TraceHeader"
    ]
    r"""<p>An X-Ray trade header, which is an http header (X-Amzn-Trace-Id) that contains the trace-id associated with the event.</p> <p>To learn more about X-Ray trace headers, see <a href=\"https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader\">Tracing header</a> in the X-Ray Developer Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventsRequestEntry) -> dict:
    out: dict = {}
    if "time" in value:
        import aws_sdk_cloudwatch_events.types.event_time

        out["Time"] = aws_sdk_cloudwatch_events.types.event_time.serialize_aws_json_1_1(
            value["time"]
        )
    if "source" in value:
        out["Source"] = value["source"]
    if "resources" in value:
        import aws_sdk_cloudwatch_events.types.event_resource_list

        out["Resources"] = (
            aws_sdk_cloudwatch_events.types.event_resource_list.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    if "detail_type" in value:
        out["DetailType"] = value["detail_type"]
    if "detail" in value:
        out["Detail"] = value["detail"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "trace_header" in value:
        out["TraceHeader"] = value["trace_header"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventsRequestEntry:
    out: PutEventsRequestEntry = {}  # type: ignore[typeddict-item]
    if "Time" in data:
        import aws_sdk_cloudwatch_events.types.event_time

        out["time"] = (
            aws_sdk_cloudwatch_events.types.event_time.deserialize_aws_json_1_1(
                data["Time"]
            )
        )
    if "Source" in data:
        out["source"] = data["Source"]
    if "Resources" in data:
        import aws_sdk_cloudwatch_events.types.event_resource_list

        out["resources"] = (
            aws_sdk_cloudwatch_events.types.event_resource_list.deserialize_aws_json_1_1(
                data["Resources"]
            )
        )
    if "DetailType" in data:
        out["detail_type"] = data["DetailType"]
    if "Detail" in data:
        out["detail"] = data["Detail"]
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    if "TraceHeader" in data:
        out["trace_header"] = data["TraceHeader"]
    return out
