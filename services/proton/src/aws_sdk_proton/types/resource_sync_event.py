"""Generated from Smithy shape ``com.amazonaws.proton#ResourceSyncEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ResourceSyncEvent(TypedDict):
    type: "str"
    """<p>The type of event.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID for the event.</p>"""
    time: "datetime.datetime"
    """<p>The time when the event occurred.</p>"""
    event: "str"
    """<p>A resource sync event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncEvent) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import aws_sdk_proton.types._prelude.timestamp

    out["time"] = aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["time"]
    )
    out["event"] = value["event"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSyncEvent:
    out: ResourceSyncEvent = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ResourceSyncEvent.type required")
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "time" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["time"] = aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["time"]
        )
    else:
        raise DeserializationError("ResourceSyncEvent.time required")
    if "event" in data:
        out["event"] = data["event"]
    else:
        raise DeserializationError("ResourceSyncEvent.event required")
    return out
