"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeEventSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_source_state
    import capo_eventbridge.types.string
    import capo_eventbridge.types.timestamp


class DescribeEventSourceResponse(TypedDict, closed=True):
    arn: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The ARN of the partner event source.</p>"""
    created_by: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The name of the SaaS partner that created the event source.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The date and time that the event source was created.</p>"""
    expiration_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The date and time that the event source will expire if you do not create a matching event bus.</p>"""
    name: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The name of the partner event source.</p>"""
    state: NotRequired["capo_eventbridge.types.event_source_state.EventSourceState"]
    """<p>The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven't yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventSourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "expiration_time" in value:
        import capo_eventbridge.types.timestamp

        out["ExpirationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["expiration_time"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        import capo_eventbridge.types.event_source_state

        out["State"] = capo_eventbridge.types.event_source_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventSourceResponse:
    out: DescribeEventSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("CreationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("ExpirationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["expiration_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("State") is not None:
        import capo_eventbridge.types.event_source_state

        out["state"] = (
            capo_eventbridge.types.event_source_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
