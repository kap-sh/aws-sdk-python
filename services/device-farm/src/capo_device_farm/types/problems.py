"""Generated from Smithy shape ``com.amazonaws.devicefarm#Problems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.problem

Problems: TypeAlias = list["capo_device_farm.types.problem.Problem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Problems) -> list:
    import capo_device_farm.types.problem

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.problem.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Problems:
    import capo_device_farm.types.problem

    out: Problems = []
    for item in data:
        out.append(capo_device_farm.types.problem.deserialize_aws_json_1_1(item))
    return out
