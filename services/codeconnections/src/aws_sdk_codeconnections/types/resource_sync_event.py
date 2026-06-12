"""Generated from Smithy shape ``com.amazonaws.codeconnections#ResourceSyncEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.event
    import aws_sdk_codeconnections.types.external_id
    import aws_sdk_codeconnections.types.timestamp
    import aws_sdk_codeconnections.types.type


class ResourceSyncEvent(TypedDict):
    event: "aws_sdk_codeconnections.types.event.Event"
    """<p>The event for a resource sync event.</p>"""
    external_id: NotRequired["aws_sdk_codeconnections.types.external_id.ExternalId"]
    """<p>The ID for a resource sync event.</p>"""
    time: "aws_sdk_codeconnections.types.timestamp.Timestamp"
    """<p>The time that a resource sync event occurred.</p>"""
    type: "aws_sdk_codeconnections.types.type.Type"
    """<p>The type of resource sync event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncEvent) -> dict:
    out: dict = {}
    out["Event"] = value["event"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    import aws_sdk_codeconnections.types.timestamp

    out["Time"] = aws_sdk_codeconnections.types.timestamp.serialize_aws_json_1_0(
        value["time"]
    )
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSyncEvent:
    out: ResourceSyncEvent = {}  # type: ignore[typeddict-item]
    if "Event" in data:
        out["event"] = data["Event"]
    else:
        raise DeserializationError("ResourceSyncEvent.event required")
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    if "Time" in data:
        import aws_sdk_codeconnections.types.timestamp

        out["time"] = aws_sdk_codeconnections.types.timestamp.deserialize_aws_json_1_0(
            data["Time"]
        )
    else:
        raise DeserializationError("ResourceSyncEvent.time required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("ResourceSyncEvent.type required")
    return out
