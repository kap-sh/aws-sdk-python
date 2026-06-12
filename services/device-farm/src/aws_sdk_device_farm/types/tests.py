"""Generated from Smithy shape ``com.amazonaws.devicefarm#Tests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.test

Tests: TypeAlias = list["aws_sdk_device_farm.types.test.Test"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tests) -> list:
    import aws_sdk_device_farm.types.test

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.test.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tests:
    import aws_sdk_device_farm.types.test

    out: Tests = []
    for item in data:
        out.append(aws_sdk_device_farm.types.test.deserialize_aws_json_1_1(item))
    return out
