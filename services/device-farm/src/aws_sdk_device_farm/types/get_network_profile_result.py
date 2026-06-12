"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetNetworkProfileResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.network_profile


class GetNetworkProfileResult(TypedDict):
    network_profile: NotRequired[
        "aws_sdk_device_farm.types.network_profile.NetworkProfile"
    ]
    """<p>The network profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNetworkProfileResult) -> dict:
    out: dict = {}
    if "network_profile" in value:
        import aws_sdk_device_farm.types.network_profile

        out["networkProfile"] = (
            aws_sdk_device_farm.types.network_profile.serialize_aws_json_1_1(
                value["network_profile"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNetworkProfileResult:
    out: GetNetworkProfileResult = {}  # type: ignore[typeddict-item]
    if "networkProfile" in data:
        import aws_sdk_device_farm.types.network_profile

        out["network_profile"] = (
            aws_sdk_device_farm.types.network_profile.deserialize_aws_json_1_1(
                data["networkProfile"]
            )
        )
    return out
