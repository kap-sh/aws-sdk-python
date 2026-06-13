"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.resource_summary

ResourceSummaryList: TypeAlias = list[
    "aws_sdk_snow_device_management.types.resource_summary.ResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSummaryList) -> list:
    import aws_sdk_snow_device_management.types.resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snow_device_management.types.resource_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourceSummaryList:
    import aws_sdk_snow_device_management.types.resource_summary

    out: ResourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_snow_device_management.types.resource_summary.deserialize_json(item)
        )
    return out
