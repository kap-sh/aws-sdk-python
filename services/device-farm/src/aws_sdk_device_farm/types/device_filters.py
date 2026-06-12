"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_filter

DeviceFilters: TypeAlias = list["aws_sdk_device_farm.types.device_filter.DeviceFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceFilters) -> list:
    import aws_sdk_device_farm.types.device_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.device_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceFilters:
    import aws_sdk_device_farm.types.device_filter

    out: DeviceFilters = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.device_filter.deserialize_aws_json_1_1(item)
        )
    return out
