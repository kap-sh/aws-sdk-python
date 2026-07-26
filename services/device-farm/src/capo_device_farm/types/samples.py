"""Generated from Smithy shape ``com.amazonaws.devicefarm#Samples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.sample

Samples: TypeAlias = list["capo_device_farm.types.sample.Sample"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Samples) -> list:
    import capo_device_farm.types.sample

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.sample.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Samples:
    import capo_device_farm.types.sample

    out: Samples = []
    for item in data:
        out.append(capo_device_farm.types.sample.deserialize_aws_json_1_1(item))
    return out
