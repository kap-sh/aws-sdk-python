"""Generated from Smithy shape ``com.amazonaws.lightsail#AddOn``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.time_of_day


class AddOn(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The name of the add-on.</p>"""
    status: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The status of the add-on.</p>"""
    snapshot_time_of_day: NotRequired["aws_sdk_lightsail.types.time_of_day.TimeOfDay"]
    """<p>The daily time when an automatic snapshot is created.</p> <p>The time shown is in <code>HH:00</code> format, and in Coordinated Universal Time (UTC).</p> <p>The snapshot is automatically created between the time shown and up to 45 minutes after.</p>"""
    next_snapshot_time_of_day: NotRequired[
        "aws_sdk_lightsail.types.time_of_day.TimeOfDay"
    ]
    """<p>The next daily time an automatic snapshot will be created.</p> <p>The time shown is in <code>HH:00</code> format, and in Coordinated Universal Time (UTC).</p> <p>The snapshot is automatically created between the time shown and up to 45 minutes after.</p>"""
    threshold: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The trigger threshold of the action.</p> <important> <p>This add-on only applies to Lightsail for Research resources.</p> </important>"""
    duration: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The amount of idle time in minutes after which your virtual computer will automatically stop.</p> <important> <p>This add-on only applies to Lightsail for Research resources.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddOn) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "snapshot_time_of_day" in value:
        out["snapshotTimeOfDay"] = value["snapshot_time_of_day"]
    if "next_snapshot_time_of_day" in value:
        out["nextSnapshotTimeOfDay"] = value["next_snapshot_time_of_day"]
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    if "duration" in value:
        out["duration"] = value["duration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddOn:
    out: AddOn = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "snapshotTimeOfDay" in data:
        out["snapshot_time_of_day"] = data["snapshotTimeOfDay"]
    if "nextSnapshotTimeOfDay" in data:
        out["next_snapshot_time_of_day"] = data["nextSnapshotTimeOfDay"]
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    if "duration" in data:
        out["duration"] = data["duration"]
    return out
