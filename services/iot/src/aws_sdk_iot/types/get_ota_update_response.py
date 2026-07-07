"""Generated from Smithy shape ``com.amazonaws.iot#GetOTAUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.ota_update_info


class GetOTAUpdateResponse(TypedDict, closed=True):
    ota_update_info: NotRequired["aws_sdk_iot.types.ota_update_info.OTAUpdateInfo"]
    """<p>The OTA update info.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOTAUpdateResponse) -> dict:
    out: dict = {}
    if "ota_update_info" in value:
        import aws_sdk_iot.types.ota_update_info

        out["otaUpdateInfo"] = aws_sdk_iot.types.ota_update_info.serialize_json(
            value["ota_update_info"]
        )
    return out


def deserialize_json(data: dict) -> GetOTAUpdateResponse:
    out: GetOTAUpdateResponse = {}  # type: ignore[typeddict-item]
    if "otaUpdateInfo" in data:
        import aws_sdk_iot.types.ota_update_info

        out["ota_update_info"] = aws_sdk_iot.types.ota_update_info.deserialize_json(
            data["otaUpdateInfo"]
        )
    return out
