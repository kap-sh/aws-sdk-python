"""Generated from Smithy shape ``com.amazonaws.mediapackage#IngressAccessLogs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class IngressAccessLogs(TypedDict):
    log_group_name: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """Customize the log group name."""


# --- restJson1 ser/de ---
def serialize_json(value: IngressAccessLogs) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> IngressAccessLogs:
    out: IngressAccessLogs = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    return out
