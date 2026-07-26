"""Generated from Smithy shape ``com.amazonaws.iotdataplane#DeleteThingShadowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.shadow_name
    import capo_iot_data_plane.types.thing_name


class DeleteThingShadowRequest(TypedDict, closed=True):
    thing_name: "capo_iot_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    shadow_name: NotRequired["capo_iot_data_plane.types.shadow_name.ShadowName"]
    """<p>The name of the shadow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThingShadowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteThingShadowRequest:
    out: DeleteThingShadowRequest = {}  # type: ignore[typeddict-item]
    return out
