"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetVPCEConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.vpce_configuration


class GetVPCEConfigurationResult(TypedDict, closed=True):
    vpce_configuration: NotRequired[
        "capo_device_farm.types.vpce_configuration.VPCEConfiguration"
    ]
    """<p>An object that contains information about your VPC endpoint configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetVPCEConfigurationResult) -> dict:
    out: dict = {}
    if "vpce_configuration" in value:
        import capo_device_farm.types.vpce_configuration

        out["vpceConfiguration"] = (
            capo_device_farm.types.vpce_configuration.serialize_aws_json_1_1(
                value["vpce_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetVPCEConfigurationResult:
    out: GetVPCEConfigurationResult = {}  # type: ignore[typeddict-item]
    if "vpceConfiguration" in data:
        import capo_device_farm.types.vpce_configuration

        out["vpce_configuration"] = (
            capo_device_farm.types.vpce_configuration.deserialize_aws_json_1_1(
                data["vpceConfiguration"]
            )
        )
    return out
