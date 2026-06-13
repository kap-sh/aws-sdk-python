"""Generated from Smithy shape ``com.amazonaws.backup#ReportPlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_plan

ReportPlanList: TypeAlias = list["aws_sdk_backup.types.report_plan.ReportPlan"]


# --- restJson1 ser/de ---
def serialize_json(value: ReportPlanList) -> list:
    import aws_sdk_backup.types.report_plan

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.report_plan.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReportPlanList:
    import aws_sdk_backup.types.report_plan

    out: ReportPlanList = []
    for item in data:
        out.append(aws_sdk_backup.types.report_plan.deserialize_json(item))
    return out
