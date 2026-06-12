"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetThingShadowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.json_document


class GetThingShadowResponse(TypedDict):
    payload: NotRequired["aws_sdk_iot_data_plane.types.json_document.JsonDocument"]
    """<p>The state information, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingShadowResponse) -> dict:
    out: dict = {}
    if "payload" in value:
        import aws_sdk_iot_data_plane.types.json_document

        out["payload"] = aws_sdk_iot_data_plane.types.json_document.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> GetThingShadowResponse:
    out: GetThingShadowResponse = {}  # type: ignore[typeddict-item]
    if "payload" in data:
        import aws_sdk_iot_data_plane.types.json_document

        out["payload"] = aws_sdk_iot_data_plane.types.json_document.deserialize_json(
            data["payload"]
        )
    return out
