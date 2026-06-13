"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.execution_summary

ExecutionSummaryList: TypeAlias = list[
    "aws_sdk_snow_device_management.types.execution_summary.ExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummaryList) -> list:
    import aws_sdk_snow_device_management.types.execution_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snow_device_management.types.execution_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExecutionSummaryList:
    import aws_sdk_snow_device_management.types.execution_summary

    out: ExecutionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_snow_device_management.types.execution_summary.deserialize_json(
                item
            )
        )
    return out
