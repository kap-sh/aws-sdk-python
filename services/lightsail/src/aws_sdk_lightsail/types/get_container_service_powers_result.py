"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServicePowersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_power_list


class GetContainerServicePowersResult(TypedDict):
    powers: NotRequired[
        "aws_sdk_lightsail.types.container_service_power_list.ContainerServicePowerList"
    ]
    """<p>An array of objects that describe the powers that can be specified for a container service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServicePowersResult) -> dict:
    out: dict = {}
    if "powers" in value:
        import aws_sdk_lightsail.types.container_service_power_list

        out["powers"] = (
            aws_sdk_lightsail.types.container_service_power_list.serialize_aws_json_1_1(
                value["powers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServicePowersResult:
    out: GetContainerServicePowersResult = {}  # type: ignore[typeddict-item]
    if "powers" in data:
        import aws_sdk_lightsail.types.container_service_power_list

        out["powers"] = (
            aws_sdk_lightsail.types.container_service_power_list.deserialize_aws_json_1_1(
                data["powers"]
            )
        )
    return out
