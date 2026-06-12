"""Generated from Smithy shape ``com.amazonaws.devicefarm#Samples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.sample

Samples: TypeAlias = list["aws_sdk_device_farm.types.sample.Sample"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Samples) -> list:
    import aws_sdk_device_farm.types.sample

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.sample.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Samples:
    import aws_sdk_device_farm.types.sample

    out: Samples = []
    for item in data:
        out.append(aws_sdk_device_farm.types.sample.deserialize_aws_json_1_1(item))
    return out
