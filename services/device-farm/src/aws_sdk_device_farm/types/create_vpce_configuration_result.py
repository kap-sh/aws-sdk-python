"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateVPCEConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.vpce_configuration


class CreateVPCEConfigurationResult(TypedDict):
    vpce_configuration: NotRequired[
        "aws_sdk_device_farm.types.vpce_configuration.VPCEConfiguration"
    ]
    """<p>An object that contains information about your VPC endpoint configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVPCEConfigurationResult) -> dict:
    out: dict = {}
    if "vpce_configuration" in value:
        import aws_sdk_device_farm.types.vpce_configuration

        out["vpceConfiguration"] = (
            aws_sdk_device_farm.types.vpce_configuration.serialize_aws_json_1_1(
                value["vpce_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVPCEConfigurationResult:
    out: CreateVPCEConfigurationResult = {}  # type: ignore[typeddict-item]
    if "vpceConfiguration" in data:
        import aws_sdk_device_farm.types.vpce_configuration

        out["vpce_configuration"] = (
            aws_sdk_device_farm.types.vpce_configuration.deserialize_aws_json_1_1(
                data["vpceConfiguration"]
            )
        )
    return out
