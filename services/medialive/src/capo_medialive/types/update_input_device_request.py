"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateInputDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.input_device_configurable_settings


class UpdateInputDeviceRequest(TypedDict, closed=True):
    hd_device_settings: NotRequired[
        "capo_medialive.types.input_device_configurable_settings.InputDeviceConfigurableSettings"
    ]
    """The settings that you want to apply to the HD input device."""
    input_device_id: "capo_medialive.types.__string.__string"
    """The unique ID of the input device. For example, hd-123456789abcdef."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """The name that you assigned to this input device (not the unique ID)."""
    uhd_device_settings: NotRequired[
        "capo_medialive.types.input_device_configurable_settings.InputDeviceConfigurableSettings"
    ]
    """The settings that you want to apply to the UHD input device."""
    availability_zone: NotRequired["capo_medialive.types.__string.__string"]
    """The Availability Zone you want associated with this input device."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInputDeviceRequest) -> dict:
    out: dict = {}
    if "hd_device_settings" in value:
        import capo_medialive.types.input_device_configurable_settings

        out["hdDeviceSettings"] = (
            capo_medialive.types.input_device_configurable_settings.serialize_json(
                value["hd_device_settings"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "uhd_device_settings" in value:
        import capo_medialive.types.input_device_configurable_settings

        out["uhdDeviceSettings"] = (
            capo_medialive.types.input_device_configurable_settings.serialize_json(
                value["uhd_device_settings"]
            )
        )
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    return out


def deserialize_json(data: dict) -> UpdateInputDeviceRequest:
    out: UpdateInputDeviceRequest = {}  # type: ignore[typeddict-item]
    if "hdDeviceSettings" in data:
        import capo_medialive.types.input_device_configurable_settings

        out["hd_device_settings"] = (
            capo_medialive.types.input_device_configurable_settings.deserialize_json(
                data["hdDeviceSettings"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "uhdDeviceSettings" in data:
        import capo_medialive.types.input_device_configurable_settings

        out["uhd_device_settings"] = (
            capo_medialive.types.input_device_configurable_settings.deserialize_json(
                data["uhdDeviceSettings"]
            )
        )
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    return out
