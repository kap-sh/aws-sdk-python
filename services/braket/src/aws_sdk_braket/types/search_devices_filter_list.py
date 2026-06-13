"""Generated from Smithy shape ``com.amazonaws.braket#SearchDevicesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.search_devices_filter

SearchDevicesFilterList: TypeAlias = list[
    "aws_sdk_braket.types.search_devices_filter.SearchDevicesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchDevicesFilterList) -> list:
    import aws_sdk_braket.types.search_devices_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.search_devices_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchDevicesFilterList:
    import aws_sdk_braket.types.search_devices_filter

    out: SearchDevicesFilterList = []
    for item in data:
        out.append(aws_sdk_braket.types.search_devices_filter.deserialize_json(item))
    return out
