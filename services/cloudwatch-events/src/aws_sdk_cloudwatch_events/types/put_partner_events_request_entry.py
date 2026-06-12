"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutPartnerEventsRequestEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.event_resource_list
    import aws_sdk_cloudwatch_events.types.event_source_name
    import aws_sdk_cloudwatch_events.types.event_time
    import aws_sdk_cloudwatch_events.types.string


class PutPartnerEventsRequestEntry(TypedDict):
    time: NotRequired["aws_sdk_cloudwatch_events.types.event_time.EventTime"]
    """<p>The date and time of the event.</p>"""
    source: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName"
    ]
    """<p>The event source that is generating the entry.</p>"""
    resources: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_resource_list.EventResourceList"
    ]
    """<p>Amazon Web Services resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.</p>"""
    detail_type: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>A free-form string used to decide what fields to expect in the event detail.</p>"""
    detail: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPartnerEventsRequestEntry) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPartnerEventsRequestEntry:
    out: PutPartnerEventsRequestEntry = {}  # type: ignore[typeddict-item]
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
    return out
