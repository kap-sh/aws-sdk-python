"""Generated from Smithy shape ``com.amazonaws.devicefarm#Offerings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering

Offerings: TypeAlias = list["aws_sdk_device_farm.types.offering.Offering"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Offerings) -> list:
    import aws_sdk_device_farm.types.offering

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.offering.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Offerings:
    import aws_sdk_device_farm.types.offering

    out: Offerings = []
    for item in data:
        out.append(aws_sdk_device_farm.types.offering.deserialize_aws_json_1_1(item))
    return out
