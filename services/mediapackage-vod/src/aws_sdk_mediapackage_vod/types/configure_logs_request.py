"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ConfigureLogsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.egress_access_logs


class ConfigureLogsRequest(TypedDict):
    egress_access_logs: NotRequired[
        "aws_sdk_mediapackage_vod.types.egress_access_logs.EgressAccessLogs"
    ]
    id: "aws_sdk_mediapackage_vod.types.__string.__string"
    """The ID of a MediaPackage VOD PackagingGroup resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsRequest) -> dict:
    out: dict = {}
    if "egress_access_logs" in value:
        import aws_sdk_mediapackage_vod.types.egress_access_logs

        out["egressAccessLogs"] = (
            aws_sdk_mediapackage_vod.types.egress_access_logs.serialize_json(
                value["egress_access_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigureLogsRequest:
    out: ConfigureLogsRequest = {}  # type: ignore[typeddict-item]
    if "egressAccessLogs" in data:
        import aws_sdk_mediapackage_vod.types.egress_access_logs

        out["egress_access_logs"] = (
            aws_sdk_mediapackage_vod.types.egress_access_logs.deserialize_json(
                data["egressAccessLogs"]
            )
        )
    return out
