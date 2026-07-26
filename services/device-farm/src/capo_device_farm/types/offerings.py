"""Generated from Smithy shape ``com.amazonaws.devicefarm#Offerings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.offering

Offerings: TypeAlias = list["capo_device_farm.types.offering.Offering"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Offerings) -> list:
    import capo_device_farm.types.offering

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.offering.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Offerings:
    import capo_device_farm.types.offering

    out: Offerings = []
    for item in data:
        out.append(capo_device_farm.types.offering.deserialize_aws_json_1_1(item))
    return out
