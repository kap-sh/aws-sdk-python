"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstanceProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.instance_profile

InstanceProfiles: TypeAlias = list[
    "capo_device_farm.types.instance_profile.InstanceProfile"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceProfiles) -> list:
    import capo_device_farm.types.instance_profile

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.instance_profile.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceProfiles:
    import capo_device_farm.types.instance_profile

    out: InstanceProfiles = []
    for item in data:
        out.append(
            capo_device_farm.types.instance_profile.deserialize_aws_json_1_1(item)
        )
    return out
