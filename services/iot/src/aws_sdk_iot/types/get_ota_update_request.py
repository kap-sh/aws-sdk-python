"""Generated from Smithy shape ``com.amazonaws.iot#GetOTAUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.ota_update_id


class GetOTAUpdateRequest(TypedDict):
    ota_update_id: "aws_sdk_iot.types.ota_update_id.OTAUpdateId"
    """<p>The OTA update ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOTAUpdateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOTAUpdateRequest:
    out: GetOTAUpdateRequest = {}  # type: ignore[typeddict-item]
    return out
