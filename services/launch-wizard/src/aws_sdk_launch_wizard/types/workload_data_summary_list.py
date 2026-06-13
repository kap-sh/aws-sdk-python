"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDataSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.workload_data_summary

WorkloadDataSummaryList: TypeAlias = list[
    "aws_sdk_launch_wizard.types.workload_data_summary.WorkloadDataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDataSummaryList) -> list:
    import aws_sdk_launch_wizard.types.workload_data_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_launch_wizard.types.workload_data_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkloadDataSummaryList:
    import aws_sdk_launch_wizard.types.workload_data_summary

    out: WorkloadDataSummaryList = []
    for item in data:
        out.append(
            aws_sdk_launch_wizard.types.workload_data_summary.deserialize_json(item)
        )
    return out
