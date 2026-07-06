"""Generated from Smithy shape ``com.amazonaws.iotdataplane#DeleteThingShadowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_data_plane.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.json_document


class DeleteThingShadowResponse(TypedDict, closed=True):
    payload: "aws_sdk_iot_data_plane.types.json_document.JsonDocument"
    """<p>The state information, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThingShadowResponse) -> dict:
    out: dict = {}
    import aws_sdk_iot_data_plane.types.json_document

    out["payload"] = aws_sdk_iot_data_plane.types.json_document.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> DeleteThingShadowResponse:
    out: DeleteThingShadowResponse = {}  # type: ignore[typeddict-item]
    if "payload" in data:
        import aws_sdk_iot_data_plane.types.json_document

        out["payload"] = aws_sdk_iot_data_plane.types.json_document.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("DeleteThingShadowResponse.payload required")
    return out
