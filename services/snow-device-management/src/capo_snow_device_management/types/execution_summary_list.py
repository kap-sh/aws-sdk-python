"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snow_device_management.types.execution_summary

ExecutionSummaryList: TypeAlias = list[
    "capo_snow_device_management.types.execution_summary.ExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummaryList) -> list:
    import capo_snow_device_management.types.execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_snow_device_management.types.execution_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExecutionSummaryList:
    import capo_snow_device_management.types.execution_summary

    out: ExecutionSummaryList = []
    for item in data:
        out.append(
            capo_snow_device_management.types.execution_summary.deserialize_json(item)
        )
    return out
