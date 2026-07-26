"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateNetworkProfileResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.network_profile


class CreateNetworkProfileResult(TypedDict, closed=True):
    network_profile: NotRequired[
        "capo_device_farm.types.network_profile.NetworkProfile"
    ]
    """<p>The network profile that is returned by the create network profile request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNetworkProfileResult) -> dict:
    out: dict = {}
    if "network_profile" in value:
        import capo_device_farm.types.network_profile

        out["networkProfile"] = (
            capo_device_farm.types.network_profile.serialize_aws_json_1_1(
                value["network_profile"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNetworkProfileResult:
    out: CreateNetworkProfileResult = {}  # type: ignore[typeddict-item]
    if "networkProfile" in data:
        import capo_device_farm.types.network_profile

        out["network_profile"] = (
            capo_device_farm.types.network_profile.deserialize_aws_json_1_1(
                data["networkProfile"]
            )
        )
    return out
