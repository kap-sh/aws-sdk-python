"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeleteCoreDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.core_device_thing_name


class DeleteCoreDeviceRequest(TypedDict, closed=True):
    core_device_thing_name: (
        "aws_sdk_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    )
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCoreDeviceRequest:
    out: DeleteCoreDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
