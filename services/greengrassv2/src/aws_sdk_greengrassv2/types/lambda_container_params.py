"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaContainerParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.lambda_device_list
    import aws_sdk_greengrassv2.types.lambda_volume_list
    import aws_sdk_greengrassv2.types.optional_boolean
    import aws_sdk_greengrassv2.types.optional_integer


class LambdaContainerParams(TypedDict, closed=True):
    memory_size_in_kb: NotRequired[
        "aws_sdk_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The memory size of the container, expressed in kilobytes.</p> <p>Default: <code>16384</code> (16 MB)</p>"""
    mount_ro_sysfs: NotRequired[
        "aws_sdk_greengrassv2.types.optional_boolean.OptionalBoolean"
    ]
    """<p>Whether or not the container can read information from the device's <code>/sys</code> folder.</p> <p>Default: <code>false</code> </p>"""
    volumes: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_volume_list.LambdaVolumeList"
    ]
    """<p>The list of volumes that the container can access.</p>"""
    devices: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_device_list.LambdaDeviceList"
    ]
    """<p>The list of system devices that the container can access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaContainerParams) -> dict:
    out: dict = {}
    if "memory_size_in_kb" in value:
        out["memorySizeInKB"] = value["memory_size_in_kb"]
    if "mount_ro_sysfs" in value:
        out["mountROSysfs"] = value["mount_ro_sysfs"]
    if "volumes" in value:
        import aws_sdk_greengrassv2.types.lambda_volume_list

        out["volumes"] = aws_sdk_greengrassv2.types.lambda_volume_list.serialize_json(
            value["volumes"]
        )
    if "devices" in value:
        import aws_sdk_greengrassv2.types.lambda_device_list

        out["devices"] = aws_sdk_greengrassv2.types.lambda_device_list.serialize_json(
            value["devices"]
        )
    return out


def deserialize_json(data: dict) -> LambdaContainerParams:
    out: LambdaContainerParams = {}  # type: ignore[typeddict-item]
    if "memorySizeInKB" in data:
        out["memory_size_in_kb"] = data["memorySizeInKB"]
    if "mountROSysfs" in data:
        out["mount_ro_sysfs"] = data["mountROSysfs"]
    if "volumes" in data:
        import aws_sdk_greengrassv2.types.lambda_volume_list

        out["volumes"] = aws_sdk_greengrassv2.types.lambda_volume_list.deserialize_json(
            data["volumes"]
        )
    if "devices" in data:
        import aws_sdk_greengrassv2.types.lambda_device_list

        out["devices"] = aws_sdk_greengrassv2.types.lambda_device_list.deserialize_json(
            data["devices"]
        )
    return out
