"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetThingShadowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.shadow_name
    import aws_sdk_iot_data_plane.types.thing_name


class GetThingShadowRequest(TypedDict):
    thing_name: "aws_sdk_iot_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    shadow_name: NotRequired["aws_sdk_iot_data_plane.types.shadow_name.ShadowName"]
    """<p>The name of the shadow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingShadowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetThingShadowRequest:
    out: GetThingShadowRequest = {}  # type: ignore[typeddict-item]
    return out
