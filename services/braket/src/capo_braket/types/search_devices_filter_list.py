"""Generated from Smithy shape ``com.amazonaws.braket#SearchDevicesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.search_devices_filter

SearchDevicesFilterList: TypeAlias = list[
    "capo_braket.types.search_devices_filter.SearchDevicesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchDevicesFilterList) -> list:
    import capo_braket.types.search_devices_filter

    out: list = []
    for item in value:
        out.append(capo_braket.types.search_devices_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchDevicesFilterList:
    import capo_braket.types.search_devices_filter

    out: SearchDevicesFilterList = []
    for item in data:
        out.append(capo_braket.types.search_devices_filter.deserialize_json(item))
    return out
