"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamDestinationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_stream_destination_status
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.string1_to1000
    import aws_sdk_customer_profiles.types.timestamp


class EventStreamDestinationDetails(TypedDict):
    uri: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.</p>"""
    status: "aws_sdk_customer_profiles.types.event_stream_destination_status.EventStreamDestinationStatus"
    """<p>The status of enabling the Kinesis stream as a destination for export.</p>"""
    unhealthy_since: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the status last changed to <code>UNHEALHY</code>.</p>"""
    message: NotRequired["aws_sdk_customer_profiles.types.string1_to1000.string1To1000"]
    """<p>The human-readable string that corresponds to the error or success while enabling the streaming destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventStreamDestinationDetails) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    import aws_sdk_customer_profiles.types.event_stream_destination_status

    out["Status"] = (
        aws_sdk_customer_profiles.types.event_stream_destination_status.serialize_json(
            value["status"]
        )
    )
    if "unhealthy_since" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["UnhealthySince"] = (
            aws_sdk_customer_profiles.types.timestamp.serialize_json(
                value["unhealthy_since"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EventStreamDestinationDetails:
    out: EventStreamDestinationDetails = {}  # type: ignore[typeddict-item]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    else:
        raise DeserializationError("EventStreamDestinationDetails.uri required")
    if "Status" in data:
        import aws_sdk_customer_profiles.types.event_stream_destination_status

        out["status"] = (
            aws_sdk_customer_profiles.types.event_stream_destination_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EventStreamDestinationDetails.status required")
    if "UnhealthySince" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["unhealthy_since"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["UnhealthySince"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
