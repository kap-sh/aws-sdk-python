"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetThingShadowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.json_document


class GetThingShadowResponse(TypedDict, closed=True):
    payload: NotRequired["capo_iot_data_plane.types.json_document.JsonDocument"]
    """<p>The state information, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingShadowResponse) -> dict:
    out: dict = {}
    if "payload" in value:
        import capo_iot_data_plane.types.json_document

        out["payload"] = capo_iot_data_plane.types.json_document.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> GetThingShadowResponse:
    out: GetThingShadowResponse = {}  # type: ignore[typeddict-item]
    if "payload" in data:
        import capo_iot_data_plane.types.json_document

        out["payload"] = capo_iot_data_plane.types.json_document.deserialize_json(
            data["payload"]
        )
    return out
