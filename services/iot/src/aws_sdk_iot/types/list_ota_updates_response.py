"""Generated from Smithy shape ``com.amazonaws.iot#ListOTAUpdatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.ota_updates_summary


class ListOTAUpdatesResponse(TypedDict):
    ota_updates: NotRequired["aws_sdk_iot.types.ota_updates_summary.OTAUpdatesSummary"]
    """<p>A list of OTA update jobs.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token to use to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOTAUpdatesResponse) -> dict:
    out: dict = {}
    if "ota_updates" in value:
        import aws_sdk_iot.types.ota_updates_summary

        out["otaUpdates"] = aws_sdk_iot.types.ota_updates_summary.serialize_json(
            value["ota_updates"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOTAUpdatesResponse:
    out: ListOTAUpdatesResponse = {}  # type: ignore[typeddict-item]
    if "otaUpdates" in data:
        import aws_sdk_iot.types.ota_updates_summary

        out["ota_updates"] = aws_sdk_iot.types.ota_updates_summary.deserialize_json(
            data["otaUpdates"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
