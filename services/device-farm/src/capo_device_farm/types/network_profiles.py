"""Generated from Smithy shape ``com.amazonaws.devicefarm#NetworkProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.network_profile

NetworkProfiles: TypeAlias = list[
    "capo_device_farm.types.network_profile.NetworkProfile"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkProfiles) -> list:
    import capo_device_farm.types.network_profile

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.network_profile.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkProfiles:
    import capo_device_farm.types.network_profile

    out: NetworkProfiles = []
    for item in data:
        out.append(
            capo_device_farm.types.network_profile.deserialize_aws_json_1_1(item)
        )
    return out
