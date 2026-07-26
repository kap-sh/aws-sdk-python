"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateInputDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__string
    import capo_medialive.types.device_settings_sync_state
    import capo_medialive.types.device_update_status
    import capo_medialive.types.input_device_connection_state
    import capo_medialive.types.input_device_hd_settings
    import capo_medialive.types.input_device_network_settings
    import capo_medialive.types.input_device_output_type
    import capo_medialive.types.input_device_type
    import capo_medialive.types.input_device_uhd_settings
    import capo_medialive.types.tags


class UpdateInputDeviceResponse(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """The unique ARN of the input device."""
    connection_state: NotRequired[
        "capo_medialive.types.input_device_connection_state.InputDeviceConnectionState"
    ]
    """The state of the connection between the input device and AWS."""
    device_settings_sync_state: NotRequired[
        "capo_medialive.types.device_settings_sync_state.DeviceSettingsSyncState"
    ]
    """The status of the action to synchronize the device configuration. If you change the configuration of the input device (for example, the maximum bitrate), MediaLive sends the new data to the device. The device might not update itself immediately. SYNCED means the device has updated its configuration. SYNCING means that it has not updated its configuration."""
    device_update_status: NotRequired[
        "capo_medialive.types.device_update_status.DeviceUpdateStatus"
    ]
    """The status of software on the input device."""
    hd_device_settings: NotRequired[
        "capo_medialive.types.input_device_hd_settings.InputDeviceHdSettings"
    ]
    """Settings that describe an input device that is type HD."""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """The unique ID of the input device."""
    mac_address: NotRequired["capo_medialive.types.__string.__string"]
    """The network MAC address of the input device."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """A name that you specify for the input device."""
    network_settings: NotRequired[
        "capo_medialive.types.input_device_network_settings.InputDeviceNetworkSettings"
    ]
    """The network settings for the input device."""
    serial_number: NotRequired["capo_medialive.types.__string.__string"]
    """The unique serial number of the input device."""
    type: NotRequired["capo_medialive.types.input_device_type.InputDeviceType"]
    """The type of the input device."""
    uhd_device_settings: NotRequired[
        "capo_medialive.types.input_device_uhd_settings.InputDeviceUhdSettings"
    ]
    """Settings that describe an input device that is type UHD."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    availability_zone: NotRequired["capo_medialive.types.__string.__string"]
    """The Availability Zone associated with this input device."""
    medialive_input_arns: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """An array of the ARNs for the MediaLive inputs attached to the device. Returned only if the outputType is MEDIALIVE_INPUT."""
    output_type: NotRequired[
        "capo_medialive.types.input_device_output_type.InputDeviceOutputType"
    ]
    """The output attachment type of the input device. Specifies MEDIACONNECT_FLOW if this device is the source for a MediaConnect flow. Specifies MEDIALIVE_INPUT if this device is the source for a MediaLive input."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInputDeviceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "connection_state" in value:
        import capo_medialive.types.input_device_connection_state

        out["connectionState"] = (
            capo_medialive.types.input_device_connection_state.serialize_json(
                value["connection_state"]
            )
        )
    if "device_settings_sync_state" in value:
        import capo_medialive.types.device_settings_sync_state

        out["deviceSettingsSyncState"] = (
            capo_medialive.types.device_settings_sync_state.serialize_json(
                value["device_settings_sync_state"]
            )
        )
    if "device_update_status" in value:
        import capo_medialive.types.device_update_status

        out["deviceUpdateStatus"] = (
            capo_medialive.types.device_update_status.serialize_json(
                value["device_update_status"]
            )
        )
    if "hd_device_settings" in value:
        import capo_medialive.types.input_device_hd_settings

        out["hdDeviceSettings"] = (
            capo_medialive.types.input_device_hd_settings.serialize_json(
                value["hd_device_settings"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "mac_address" in value:
        out["macAddress"] = value["mac_address"]
    if "name" in value:
        out["name"] = value["name"]
    if "network_settings" in value:
        import capo_medialive.types.input_device_network_settings

        out["networkSettings"] = (
            capo_medialive.types.input_device_network_settings.serialize_json(
                value["network_settings"]
            )
        )
    if "serial_number" in value:
        out["serialNumber"] = value["serial_number"]
    if "type" in value:
        import capo_medialive.types.input_device_type

        out["type"] = capo_medialive.types.input_device_type.serialize_json(
            value["type"]
        )
    if "uhd_device_settings" in value:
        import capo_medialive.types.input_device_uhd_settings

        out["uhdDeviceSettings"] = (
            capo_medialive.types.input_device_uhd_settings.serialize_json(
                value["uhd_device_settings"]
            )
        )
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "medialive_input_arns" in value:
        import capo_medialive.types.__list_of__string

        out["medialiveInputArns"] = (
            capo_medialive.types.__list_of__string.serialize_json(
                value["medialive_input_arns"]
            )
        )
    if "output_type" in value:
        import capo_medialive.types.input_device_output_type

        out["outputType"] = (
            capo_medialive.types.input_device_output_type.serialize_json(
                value["output_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateInputDeviceResponse:
    out: UpdateInputDeviceResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "connectionState" in data:
        import capo_medialive.types.input_device_connection_state

        out["connection_state"] = (
            capo_medialive.types.input_device_connection_state.deserialize_json(
                data["connectionState"]
            )
        )
    if "deviceSettingsSyncState" in data:
        import capo_medialive.types.device_settings_sync_state

        out["device_settings_sync_state"] = (
            capo_medialive.types.device_settings_sync_state.deserialize_json(
                data["deviceSettingsSyncState"]
            )
        )
    if "deviceUpdateStatus" in data:
        import capo_medialive.types.device_update_status

        out["device_update_status"] = (
            capo_medialive.types.device_update_status.deserialize_json(
                data["deviceUpdateStatus"]
            )
        )
    if "hdDeviceSettings" in data:
        import capo_medialive.types.input_device_hd_settings

        out["hd_device_settings"] = (
            capo_medialive.types.input_device_hd_settings.deserialize_json(
                data["hdDeviceSettings"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "macAddress" in data:
        out["mac_address"] = data["macAddress"]
    if "name" in data:
        out["name"] = data["name"]
    if "networkSettings" in data:
        import capo_medialive.types.input_device_network_settings

        out["network_settings"] = (
            capo_medialive.types.input_device_network_settings.deserialize_json(
                data["networkSettings"]
            )
        )
    if "serialNumber" in data:
        out["serial_number"] = data["serialNumber"]
    if "type" in data:
        import capo_medialive.types.input_device_type

        out["type"] = capo_medialive.types.input_device_type.deserialize_json(
            data["type"]
        )
    if "uhdDeviceSettings" in data:
        import capo_medialive.types.input_device_uhd_settings

        out["uhd_device_settings"] = (
            capo_medialive.types.input_device_uhd_settings.deserialize_json(
                data["uhdDeviceSettings"]
            )
        )
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "medialiveInputArns" in data:
        import capo_medialive.types.__list_of__string

        out["medialive_input_arns"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["medialiveInputArns"]
            )
        )
    if "outputType" in data:
        import capo_medialive.types.input_device_output_type

        out["output_type"] = (
            capo_medialive.types.input_device_output_type.deserialize_json(
                data["outputType"]
            )
        )
    return out
