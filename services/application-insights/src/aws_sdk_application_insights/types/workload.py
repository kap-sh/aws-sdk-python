"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Workload``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.component_name
    import aws_sdk_application_insights.types.missing_workload_config
    import aws_sdk_application_insights.types.remarks
    import aws_sdk_application_insights.types.tier
    import aws_sdk_application_insights.types.workload_id
    import aws_sdk_application_insights.types.workload_name


class Workload(TypedDict):
    workload_id: NotRequired[
        "aws_sdk_application_insights.types.workload_id.WorkloadId"
    ]
    """<p>The ID of the workload.</p>"""
    component_name: NotRequired[
        "aws_sdk_application_insights.types.component_name.ComponentName"
    ]
    """<p>The name of the component.</p>"""
    workload_name: NotRequired[
        "aws_sdk_application_insights.types.workload_name.WorkloadName"
    ]
    """<p>The name of the workload.</p>"""
    tier: NotRequired["aws_sdk_application_insights.types.tier.Tier"]
    """<p>The tier of the workload.</p>"""
    workload_remarks: NotRequired["aws_sdk_application_insights.types.remarks.Remarks"]
    """<p>If logging is supported for the resource type, shows whether the component has configured logs to be monitored.</p>"""
    missing_workload_config: NotRequired[
        "aws_sdk_application_insights.types.missing_workload_config.MissingWorkloadConfig"
    ]
    """<p>Indicates whether all of the component configurations required to monitor a workload were provided.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workload) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "tier" in value:
        import aws_sdk_application_insights.types.tier

        out["Tier"] = aws_sdk_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "workload_remarks" in value:
        out["WorkloadRemarks"] = value["workload_remarks"]
    if "missing_workload_config" in value:
        out["MissingWorkloadConfig"] = value["missing_workload_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Workload:
    out: Workload = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "Tier" in data:
        import aws_sdk_application_insights.types.tier

        out["tier"] = aws_sdk_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if "WorkloadRemarks" in data:
        out["workload_remarks"] = data["WorkloadRemarks"]
    if "MissingWorkloadConfig" in data:
        out["missing_workload_config"] = data["MissingWorkloadConfig"]
    return out
