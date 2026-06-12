"""Generated from Smithy shape ``com.amazonaws.medialive#EpochLockingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class EpochLockingSettings(TypedDict):
    custom_epoch: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Optional. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00."""
    jam_sync_time: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Optional. Enter a time for the jam sync. The default is midnight UTC. When epoch locking is enabled, MediaLive performs a daily jam sync on every output encode to ensure timecodes don’t diverge from the wall clock. The jam sync applies only to encodes with frame rate of 29.97 or 59.94 FPS. To override, enter a time in HH:MM:SS in UTC. Always set the MM:SS portion to 00:00."""


# --- restJson1 ser/de ---
def serialize_json(value: EpochLockingSettings) -> dict:
    out: dict = {}
    if "custom_epoch" in value:
        out["customEpoch"] = value["custom_epoch"]
    if "jam_sync_time" in value:
        out["jamSyncTime"] = value["jam_sync_time"]
    return out


def deserialize_json(data: dict) -> EpochLockingSettings:
    out: EpochLockingSettings = {}  # type: ignore[typeddict-item]
    if "customEpoch" in data:
        out["custom_epoch"] = data["customEpoch"]
    if "jamSyncTime" in data:
        out["jam_sync_time"] = data["jamSyncTime"]
    return out
