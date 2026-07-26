"""Generated from Smithy shape ``com.amazonaws.devicefarm#Runs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.run

Runs: TypeAlias = list["capo_device_farm.types.run.Run"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Runs) -> list:
    import capo_device_farm.types.run

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Runs:
    import capo_device_farm.types.run

    out: Runs = []
    for item in data:
        out.append(capo_device_farm.types.run.deserialize_aws_json_1_1(item))
    return out
