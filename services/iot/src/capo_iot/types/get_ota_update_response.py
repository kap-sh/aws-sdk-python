"""Generated from Smithy shape ``com.amazonaws.iot#GetOTAUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ota_update_info


class GetOTAUpdateResponse(TypedDict, closed=True):
    ota_update_info: NotRequired["capo_iot.types.ota_update_info.OTAUpdateInfo"]
    """<p>The OTA update info.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOTAUpdateResponse) -> dict:
    out: dict = {}
    if "ota_update_info" in value:
        import capo_iot.types.ota_update_info

        out["otaUpdateInfo"] = capo_iot.types.ota_update_info.serialize_json(
            value["ota_update_info"]
        )
    return out


def deserialize_json(data: dict) -> GetOTAUpdateResponse:
    out: GetOTAUpdateResponse = {}  # type: ignore[typeddict-item]
    if "otaUpdateInfo" in data:
        import capo_iot.types.ota_update_info

        out["ota_update_info"] = capo_iot.types.ota_update_info.deserialize_json(
            data["otaUpdateInfo"]
        )
    return out
