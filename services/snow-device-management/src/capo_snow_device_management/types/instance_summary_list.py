"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#InstanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snow_device_management.types.instance_summary

InstanceSummaryList: TypeAlias = list[
    "capo_snow_device_management.types.instance_summary.InstanceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceSummaryList) -> list:
    import capo_snow_device_management.types.instance_summary

    out: list = []
    for item in value:
        out.append(
            capo_snow_device_management.types.instance_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InstanceSummaryList:
    import capo_snow_device_management.types.instance_summary

    out: InstanceSummaryList = []
    for item in data:
        out.append(
            capo_snow_device_management.types.instance_summary.deserialize_json(item)
        )
    return out
