"""Generated from Smithy shape ``com.amazonaws.medialive#RebootInputDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.reboot_input_device_force


class RebootInputDeviceRequest(TypedDict, closed=True):
    force: NotRequired[
        "capo_medialive.types.reboot_input_device_force.RebootInputDeviceForce"
    ]
    """Force a reboot of an input device. If the device is streaming, it will stop streaming and begin rebooting within a few seconds of sending the command. If the device was streaming prior to the reboot, the device will resume streaming when the reboot completes."""
    input_device_id: "capo_medialive.types.__string.__string"
    """The unique ID of the input device to reboot. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: RebootInputDeviceRequest) -> dict:
    out: dict = {}
    if "force" in value:
        import capo_medialive.types.reboot_input_device_force

        out["force"] = capo_medialive.types.reboot_input_device_force.serialize_json(
            value["force"]
        )
    return out


def deserialize_json(data: dict) -> RebootInputDeviceRequest:
    out: RebootInputDeviceRequest = {}  # type: ignore[typeddict-item]
    if "force" in data:
        import capo_medialive.types.reboot_input_device_force

        out["force"] = capo_medialive.types.reboot_input_device_force.deserialize_json(
            data["force"]
        )
    return out
