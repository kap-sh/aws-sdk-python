"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.destination_summary
    import aws_sdk_customer_profiles.types.event_stream_state
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp


class EventStreamSummary(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_stream_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the event stream.</p>"""
    event_stream_arn: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>A unique identifier for the event stream.</p>"""
    state: "aws_sdk_customer_profiles.types.event_stream_state.EventStreamState"
    """<p>The operational state of destination stream for export.</p>"""
    stopped_since: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the <code>State</code> changed to <code>STOPPED</code>.</p>"""
    destination_summary: NotRequired[
        "aws_sdk_customer_profiles.types.destination_summary.DestinationSummary"
    ]
    """<p>Summary information about the Kinesis data stream.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventStreamSummary) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["EventStreamName"] = value["event_stream_name"]
    out["EventStreamArn"] = value["event_stream_arn"]
    import aws_sdk_customer_profiles.types.event_stream_state

    out["State"] = aws_sdk_customer_profiles.types.event_stream_state.serialize_json(
        value["state"]
    )
    if "stopped_since" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["StoppedSince"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["stopped_since"]
        )
    if "destination_summary" in value:
        import aws_sdk_customer_profiles.types.destination_summary

        out["DestinationSummary"] = (
            aws_sdk_customer_profiles.types.destination_summary.serialize_json(
                value["destination_summary"]
            )
        )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> EventStreamSummary:
    out: EventStreamSummary = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("EventStreamSummary.domain_name required")
    if "EventStreamName" in data:
        out["event_stream_name"] = data["EventStreamName"]
    else:
        raise DeserializationError("EventStreamSummary.event_stream_name required")
    if "EventStreamArn" in data:
        out["event_stream_arn"] = data["EventStreamArn"]
    else:
        raise DeserializationError("EventStreamSummary.event_stream_arn required")
    if "State" in data:
        import aws_sdk_customer_profiles.types.event_stream_state

        out["state"] = (
            aws_sdk_customer_profiles.types.event_stream_state.deserialize_json(
                data["State"]
            )
        )
    else:
        raise DeserializationError("EventStreamSummary.state required")
    if "StoppedSince" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["stopped_since"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["StoppedSince"]
            )
        )
    if "DestinationSummary" in data:
        import aws_sdk_customer_profiles.types.destination_summary

        out["destination_summary"] = (
            aws_sdk_customer_profiles.types.destination_summary.deserialize_json(
                data["DestinationSummary"]
            )
        )
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
