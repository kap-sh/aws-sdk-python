"""Generated from Smithy shape ``com.amazonaws.devicefarm#Tests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.test

Tests: TypeAlias = list["capo_device_farm.types.test.Test"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tests) -> list:
    import capo_device_farm.types.test

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.test.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tests:
    import capo_device_farm.types.test

    out: Tests = []
    for item in data:
        out.append(capo_device_farm.types.test.deserialize_aws_json_1_1(item))
    return out
