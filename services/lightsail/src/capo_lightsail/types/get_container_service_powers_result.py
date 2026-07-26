"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServicePowersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_power_list


class GetContainerServicePowersResult(TypedDict, closed=True):
    powers: NotRequired[
        "capo_lightsail.types.container_service_power_list.ContainerServicePowerList"
    ]
    """<p>An array of objects that describe the powers that can be specified for a container service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServicePowersResult) -> dict:
    out: dict = {}
    if "powers" in value:
        import capo_lightsail.types.container_service_power_list

        out["powers"] = (
            capo_lightsail.types.container_service_power_list.serialize_aws_json_1_1(
                value["powers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServicePowersResult:
    out: GetContainerServicePowersResult = {}  # type: ignore[typeddict-item]
    if "powers" in data:
        import capo_lightsail.types.container_service_power_list

        out["powers"] = (
            capo_lightsail.types.container_service_power_list.deserialize_aws_json_1_1(
                data["powers"]
            )
        )
    return out
