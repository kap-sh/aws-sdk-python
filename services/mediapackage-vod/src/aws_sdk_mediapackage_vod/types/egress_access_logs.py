"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#EgressAccessLogs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string


class EgressAccessLogs(TypedDict):
    log_group_name: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """Customize the log group name."""


# --- restJson1 ser/de ---
def serialize_json(value: EgressAccessLogs) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> EgressAccessLogs:
    out: EgressAccessLogs = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    return out
