"""Generated from Smithy shape ``com.amazonaws.devicefarm#Suites``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.suite

Suites: TypeAlias = list["aws_sdk_device_farm.types.suite.Suite"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Suites) -> list:
    import aws_sdk_device_farm.types.suite

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.suite.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Suites:
    import aws_sdk_device_farm.types.suite

    out: Suites = []
    for item in data:
        out.append(aws_sdk_device_farm.types.suite.deserialize_aws_json_1_1(item))
    return out
