"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePoolCompatibilityResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.device_pool_compatibility_result

DevicePoolCompatibilityResults: TypeAlias = list[
    "capo_device_farm.types.device_pool_compatibility_result.DevicePoolCompatibilityResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevicePoolCompatibilityResults) -> list:
    import capo_device_farm.types.device_pool_compatibility_result

    out: list = []
    for item in value:
        out.append(
            capo_device_farm.types.device_pool_compatibility_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DevicePoolCompatibilityResults:
    import capo_device_farm.types.device_pool_compatibility_result

    out: DevicePoolCompatibilityResults = []
    for item in data:
        out.append(
            capo_device_farm.types.device_pool_compatibility_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
