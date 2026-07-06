"""Generated from Smithy shape ``com.amazonaws.medialive#DisabledLockingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DisabledLockingSettings(TypedDict, closed=True):
    custom_epoch: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Optional. Only applies to CMAF Ingest Output Group and MediaPackage V2 Output Group. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00."""


# --- restJson1 ser/de ---
def serialize_json(value: DisabledLockingSettings) -> dict:
    out: dict = {}
    if "custom_epoch" in value:
        out["customEpoch"] = value["custom_epoch"]
    return out


def deserialize_json(data: dict) -> DisabledLockingSettings:
    out: DisabledLockingSettings = {}  # type: ignore[typeddict-item]
    if "customEpoch" in data:
        out["custom_epoch"] = data["customEpoch"]
    return out
