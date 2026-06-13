"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#Command``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_snow_device_management.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.reboot
    import aws_sdk_snow_device_management.types.unlock


class _Command_unlock(TypedDict):
    unlock: "aws_sdk_snow_device_management.types.unlock.Unlock"


class _Command_reboot(TypedDict):
    reboot: "aws_sdk_snow_device_management.types.reboot.Reboot"


Command: TypeAlias = _Command_unlock | _Command_reboot


# --- restJson1 ser/de ---
def serialize_json(value: Command) -> dict:
    if "unlock" in value:
        import aws_sdk_snow_device_management.types.unlock

        return {
            "unlock": aws_sdk_snow_device_management.types.unlock.serialize_json(
                value["unlock"]
            )
        }
    elif "reboot" in value:
        import aws_sdk_snow_device_management.types.reboot

        return {
            "reboot": aws_sdk_snow_device_management.types.reboot.serialize_json(
                value["reboot"]
            )
        }
    else:
        raise SerializationError("Command: no variant present")


def deserialize_json(data: dict) -> Command:
    if "unlock" in data:
        import aws_sdk_snow_device_management.types.unlock

        return {
            "unlock": aws_sdk_snow_device_management.types.unlock.deserialize_json(
                data["unlock"]
            )
        }
    elif "reboot" in data:
        import aws_sdk_snow_device_management.types.reboot

        return {
            "reboot": aws_sdk_snow_device_management.types.reboot.deserialize_json(
                data["reboot"]
            )
        }
    else:
        raise DeserializationError("Command: no recognized variant key")
