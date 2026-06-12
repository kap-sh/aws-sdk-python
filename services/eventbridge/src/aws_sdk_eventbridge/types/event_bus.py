"""Generated from Smithy shape ``com.amazonaws.eventbridge#EventBus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_bus_description
    import aws_sdk_eventbridge.types.string
    import aws_sdk_eventbridge.types.timestamp


class EventBus(TypedDict):
    name: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The name of the event bus.</p>"""
    arn: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The ARN of the event bus.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.event_bus_description.EventBusDescription"
    ]
    """<p>The event bus description.</p>"""
    policy: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The permissions policy of the event bus, describing which other Amazon Web Services accounts can write events to this event bus.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventBus) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventBus:
    out: EventBus = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
