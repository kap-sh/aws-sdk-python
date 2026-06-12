"""Generated from Smithy shape ``com.amazonaws.devicefarm#Problems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.problem

Problems: TypeAlias = list["aws_sdk_device_farm.types.problem.Problem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Problems) -> list:
    import aws_sdk_device_farm.types.problem

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.problem.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Problems:
    import aws_sdk_device_farm.types.problem

    out: Problems = []
    for item in data:
        out.append(aws_sdk_device_farm.types.problem.deserialize_aws_json_1_1(item))
    return out
