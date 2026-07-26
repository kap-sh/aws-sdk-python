"""Generated from Smithy shape ``com.amazonaws.iot#GetOTAUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ota_update_id


class GetOTAUpdateRequest(TypedDict, closed=True):
    ota_update_id: "capo_iot.types.ota_update_id.OTAUpdateId"
    """<p>The OTA update ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOTAUpdateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOTAUpdateRequest:
    out: GetOTAUpdateRequest = {}  # type: ignore[typeddict-item]
    return out
