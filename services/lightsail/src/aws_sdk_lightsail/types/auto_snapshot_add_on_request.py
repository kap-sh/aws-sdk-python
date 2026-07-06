"""Generated from Smithy shape ``com.amazonaws.lightsail#AutoSnapshotAddOnRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.time_of_day


class AutoSnapshotAddOnRequest(TypedDict, closed=True):
    snapshot_time_of_day: NotRequired["aws_sdk_lightsail.types.time_of_day.TimeOfDay"]
    """<p>The daily time when an automatic snapshot will be created.</p> <p>Constraints:</p> <ul> <li> <p>Must be in <code>HH:00</code> format, and in an hourly increment.</p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>The snapshot will be automatically created between the time specified and up to 45 minutes after.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoSnapshotAddOnRequest) -> dict:
    out: dict = {}
    if "snapshot_time_of_day" in value:
        out["snapshotTimeOfDay"] = value["snapshot_time_of_day"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoSnapshotAddOnRequest:
    out: AutoSnapshotAddOnRequest = {}  # type: ignore[typeddict-item]
    if "snapshotTimeOfDay" in data:
        out["snapshot_time_of_day"] = data["snapshotTimeOfDay"]
    return out
