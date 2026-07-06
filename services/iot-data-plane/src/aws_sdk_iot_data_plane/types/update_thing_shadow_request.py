"""Generated from Smithy shape ``com.amazonaws.iotdataplane#UpdateThingShadowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_data_plane.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.json_document
    import aws_sdk_iot_data_plane.types.shadow_name
    import aws_sdk_iot_data_plane.types.thing_name


class UpdateThingShadowRequest(TypedDict, closed=True):
    thing_name: "aws_sdk_iot_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    shadow_name: NotRequired["aws_sdk_iot_data_plane.types.shadow_name.ShadowName"]
    """<p>The name of the shadow.</p>"""
    payload: "aws_sdk_iot_data_plane.types.json_document.JsonDocument"
    """<p>The state information, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingShadowRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_data_plane.types.json_document

    out["payload"] = aws_sdk_iot_data_plane.types.json_document.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> UpdateThingShadowRequest:
    out: UpdateThingShadowRequest = {}  # type: ignore[typeddict-item]
    if "payload" in data:
        import aws_sdk_iot_data_plane.types.json_document

        out["payload"] = aws_sdk_iot_data_plane.types.json_document.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("UpdateThingShadowRequest.payload required")
    return out
