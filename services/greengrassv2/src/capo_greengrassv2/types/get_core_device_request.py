"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetCoreDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.core_device_thing_name


class GetCoreDeviceRequest(TypedDict, closed=True):
    core_device_thing_name: (
        "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    )
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCoreDeviceRequest:
    out: GetCoreDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
