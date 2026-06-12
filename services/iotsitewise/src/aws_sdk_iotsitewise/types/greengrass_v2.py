"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GreengrassV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.core_device_operating_system
    import aws_sdk_iotsitewise.types.core_device_thing_name


class GreengrassV2(TypedDict):
    core_device_thing_name: (
        "aws_sdk_iotsitewise.types.core_device_thing_name.CoreDeviceThingName"
    )
    """<p>The name of the IoT thing for your IoT Greengrass V2 core device.</p>"""
    core_device_operating_system: NotRequired[
        "aws_sdk_iotsitewise.types.core_device_operating_system.CoreDeviceOperatingSystem"
    ]
    """<p>The operating system of the core device in IoT Greengrass V2. Specifying the operating system is required for MQTT-enabled, V3 gateways (<code>gatewayVersion</code> <code>3</code>) and not applicable for Classic stream, V2 gateways (<code>gatewayVersion</code> <code>2</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GreengrassV2) -> dict:
    out: dict = {}
    out["coreDeviceThingName"] = value["core_device_thing_name"]
    if "core_device_operating_system" in value:
        import aws_sdk_iotsitewise.types.core_device_operating_system

        out["coreDeviceOperatingSystem"] = (
            aws_sdk_iotsitewise.types.core_device_operating_system.serialize_json(
                value["core_device_operating_system"]
            )
        )
    return out


def deserialize_json(data: dict) -> GreengrassV2:
    out: GreengrassV2 = {}  # type: ignore[typeddict-item]
    if "coreDeviceThingName" in data:
        out["core_device_thing_name"] = data["coreDeviceThingName"]
    else:
        raise DeserializationError("GreengrassV2.core_device_thing_name required")
    if "coreDeviceOperatingSystem" in data:
        import aws_sdk_iotsitewise.types.core_device_operating_system

        out["core_device_operating_system"] = (
            aws_sdk_iotsitewise.types.core_device_operating_system.deserialize_json(
                data["coreDeviceOperatingSystem"]
            )
        )
    return out
