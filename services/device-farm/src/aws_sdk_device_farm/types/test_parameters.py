"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.string

TestParameters: TypeAlias = dict[
    "aws_sdk_device_farm.types.string.String", "aws_sdk_device_farm.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TestParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TestParameters:
    out: TestParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
