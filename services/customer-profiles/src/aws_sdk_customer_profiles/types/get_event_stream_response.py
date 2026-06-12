"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetEventStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_stream_destination_details
    import aws_sdk_customer_profiles.types.event_stream_state
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp


class GetEventStreamResponse(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_stream_arn: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>A unique identifier for the event stream.</p>"""
    created_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the export was created.</p>"""
    state: "aws_sdk_customer_profiles.types.event_stream_state.EventStreamState"
    """<p>The operational state of destination stream for export.</p>"""
    stopped_since: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the <code>State</code> changed to <code>STOPPED</code>.</p>"""
    destination_details: "aws_sdk_customer_profiles.types.event_stream_destination_details.EventStreamDestinationDetails"
    """<p>Details regarding the Kinesis stream.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventStreamResponse) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["EventStreamArn"] = value["event_stream_arn"]
    import aws_sdk_customer_profiles.types.timestamp

    out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_customer_profiles.types.event_stream_state

    out["State"] = aws_sdk_customer_profiles.types.event_stream_state.serialize_json(
        value["state"]
    )
    if "stopped_since" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["StoppedSince"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["stopped_since"]
        )
    import aws_sdk_customer_profiles.types.event_stream_destination_details

    out["DestinationDetails"] = (
        aws_sdk_customer_profiles.types.event_stream_destination_details.serialize_json(
            value["destination_details"]
        )
    )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetEventStreamResponse:
    out: GetEventStreamResponse = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("GetEventStreamResponse.domain_name required")
    if "EventStreamArn" in data:
        out["event_stream_arn"] = data["EventStreamArn"]
    else:
        raise DeserializationError("GetEventStreamResponse.event_stream_arn required")
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("GetEventStreamResponse.created_at required")
    if "State" in data:
        import aws_sdk_customer_profiles.types.event_stream_state

        out["state"] = (
            aws_sdk_customer_profiles.types.event_stream_state.deserialize_json(
                data["State"]
            )
        )
    else:
        raise DeserializationError("GetEventStreamResponse.state required")
    if "StoppedSince" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["stopped_since"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["StoppedSince"]
            )
        )
    if "DestinationDetails" in data:
        import aws_sdk_customer_profiles.types.event_stream_destination_details

        out["destination_details"] = (
            aws_sdk_customer_profiles.types.event_stream_destination_details.deserialize_json(
                data["DestinationDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetEventStreamResponse.destination_details required"
        )
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
