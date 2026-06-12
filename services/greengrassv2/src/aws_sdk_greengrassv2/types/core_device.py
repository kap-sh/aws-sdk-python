"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CoreDevice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.core_device_architecture_string
    import aws_sdk_greengrassv2.types.core_device_platform_string
    import aws_sdk_greengrassv2.types.core_device_runtime_string
    import aws_sdk_greengrassv2.types.core_device_status
    import aws_sdk_greengrassv2.types.core_device_thing_name
    import aws_sdk_greengrassv2.types.timestamp


class CoreDevice(TypedDict):
    core_device_thing_name: NotRequired[
        "aws_sdk_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    ]
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""
    status: NotRequired[
        "aws_sdk_greengrassv2.types.core_device_status.CoreDeviceStatus"
    ]
    """<p>The status of the core device. Core devices can have the following statuses:</p> <ul> <li> <p> <code>HEALTHY</code> – The IoT Greengrass Core software and all components run on the core device without issue.</p> </li> <li> <p> <code>UNHEALTHY</code> – The IoT Greengrass Core software or a component is in a failed state on the core device.</p> </li> </ul>"""
    last_status_update_timestamp: NotRequired[
        "aws_sdk_greengrassv2.types.timestamp.Timestamp"
    ]
    """<p>The time at which the core device's status last updated, expressed in ISO 8601 format.</p>"""
    platform: NotRequired[
        "aws_sdk_greengrassv2.types.core_device_platform_string.CoreDevicePlatformString"
    ]
    """<p>The operating system platform that the core device runs.</p>"""
    architecture: NotRequired[
        "aws_sdk_greengrassv2.types.core_device_architecture_string.CoreDeviceArchitectureString"
    ]
    """<p>The computer architecture of the core device.</p>"""
    runtime: NotRequired[
        "aws_sdk_greengrassv2.types.core_device_runtime_string.CoreDeviceRuntimeString"
    ]
    """<p>The runtime for the core device. The runtime can be:</p> <ul> <li> <p> <code>aws_nucleus_classic</code> </p> </li> <li> <p> <code>aws_nucleus_lite</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreDevice) -> dict:
    out: dict = {}
    if "core_device_thing_name" in value:
        out["coreDeviceThingName"] = value["core_device_thing_name"]
    if "status" in value:
        import aws_sdk_greengrassv2.types.core_device_status

        out["status"] = aws_sdk_greengrassv2.types.core_device_status.serialize_json(
            value["status"]
        )
    if "last_status_update_timestamp" in value:
        import aws_sdk_greengrassv2.types.timestamp

        out["lastStatusUpdateTimestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.serialize_json(
                value["last_status_update_timestamp"]
            )
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    return out


def deserialize_json(data: dict) -> CoreDevice:
    out: CoreDevice = {}  # type: ignore[typeddict-item]
    if "coreDeviceThingName" in data:
        out["core_device_thing_name"] = data["coreDeviceThingName"]
    if "status" in data:
        import aws_sdk_greengrassv2.types.core_device_status

        out["status"] = aws_sdk_greengrassv2.types.core_device_status.deserialize_json(
            data["status"]
        )
    if "lastStatusUpdateTimestamp" in data:
        import aws_sdk_greengrassv2.types.timestamp

        out["last_status_update_timestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.deserialize_json(
                data["lastStatusUpdateTimestamp"]
            )
        )
    if "platform" in data:
        out["platform"] = data["platform"]
    if "architecture" in data:
        out["architecture"] = data["architecture"]
    if "runtime" in data:
        out["runtime"] = data["runtime"]
    return out
