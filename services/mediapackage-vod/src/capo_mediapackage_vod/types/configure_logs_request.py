"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ConfigureLogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.egress_access_logs


class ConfigureLogsRequest(TypedDict, closed=True):
    egress_access_logs: NotRequired[
        "capo_mediapackage_vod.types.egress_access_logs.EgressAccessLogs"
    ]
    id: "capo_mediapackage_vod.types.__string.__string"
    """The ID of a MediaPackage VOD PackagingGroup resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsRequest) -> dict:
    out: dict = {}
    if "egress_access_logs" in value:
        import capo_mediapackage_vod.types.egress_access_logs

        out["egressAccessLogs"] = (
            capo_mediapackage_vod.types.egress_access_logs.serialize_json(
                value["egress_access_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigureLogsRequest:
    out: ConfigureLogsRequest = {}  # type: ignore[typeddict-item]
    if "egressAccessLogs" in data:
        import capo_mediapackage_vod.types.egress_access_logs

        out["egress_access_logs"] = (
            capo_mediapackage_vod.types.egress_access_logs.deserialize_json(
                data["egressAccessLogs"]
            )
        )
    return out
