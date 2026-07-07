"""Generated from Smithy shape ``com.amazonaws.snowball#DeviceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.snowcone_device_configuration


class DeviceConfiguration(TypedDict, closed=True):
    snowcone_device_configuration: NotRequired[
        "aws_sdk_snowball.types.snowcone_device_configuration.SnowconeDeviceConfiguration"
    ]
    """<p>Returns information about the device configuration for an Snowball Edge job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceConfiguration) -> dict:
    out: dict = {}
    if "snowcone_device_configuration" in value:
        import aws_sdk_snowball.types.snowcone_device_configuration

        out["SnowconeDeviceConfiguration"] = (
            aws_sdk_snowball.types.snowcone_device_configuration.serialize_aws_json_1_1(
                value["snowcone_device_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceConfiguration:
    out: DeviceConfiguration = {}  # type: ignore[typeddict-item]
    if "SnowconeDeviceConfiguration" in data:
        import aws_sdk_snowball.types.snowcone_device_configuration

        out["snowcone_device_configuration"] = (
            aws_sdk_snowball.types.snowcone_device_configuration.deserialize_aws_json_1_1(
                data["SnowconeDeviceConfiguration"]
            )
        )
    return out
