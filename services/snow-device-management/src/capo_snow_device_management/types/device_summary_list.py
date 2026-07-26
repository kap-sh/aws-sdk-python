"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DeviceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snow_device_management.types.device_summary

DeviceSummaryList: TypeAlias = list[
    "capo_snow_device_management.types.device_summary.DeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceSummaryList) -> list:
    import capo_snow_device_management.types.device_summary

    out: list = []
    for item in value:
        out.append(
            capo_snow_device_management.types.device_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeviceSummaryList:
    import capo_snow_device_management.types.device_summary

    out: DeviceSummaryList = []
    for item in data:
        out.append(
            capo_snow_device_management.types.device_summary.deserialize_json(item)
        )
    return out
