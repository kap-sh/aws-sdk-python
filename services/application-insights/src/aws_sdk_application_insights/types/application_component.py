"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ApplicationComponent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.component_name
    import aws_sdk_application_insights.types.detected_workload
    import aws_sdk_application_insights.types.monitor
    import aws_sdk_application_insights.types.os_type
    import aws_sdk_application_insights.types.remarks
    import aws_sdk_application_insights.types.resource_type
    import aws_sdk_application_insights.types.tier


class ApplicationComponent(TypedDict):
    component_name: NotRequired[
        "aws_sdk_application_insights.types.component_name.ComponentName"
    ]
    """<p>The name of the component.</p>"""
    component_remarks: NotRequired["aws_sdk_application_insights.types.remarks.Remarks"]
    """<p> If logging is supported for the resource type, indicates whether the component has configured logs to be monitored. </p>"""
    resource_type: NotRequired[
        "aws_sdk_application_insights.types.resource_type.ResourceType"
    ]
    """<p>The resource type. Supported resource types include EC2 instances, Auto Scaling group, Classic ELB, Application ELB, and SQS Queue.</p>"""
    os_type: NotRequired["aws_sdk_application_insights.types.os_type.OsType"]
    """<p> The operating system of the component. </p>"""
    tier: NotRequired["aws_sdk_application_insights.types.tier.Tier"]
    """<p>The stack tier of the application component.</p>"""
    monitor: NotRequired["aws_sdk_application_insights.types.monitor.Monitor"]
    """<p>Indicates whether the application component is monitored. </p>"""
    detected_workload: NotRequired[
        "aws_sdk_application_insights.types.detected_workload.DetectedWorkload"
    ]
    """<p> Workloads detected in the application component. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationComponent) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "component_remarks" in value:
        out["ComponentRemarks"] = value["component_remarks"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "os_type" in value:
        import aws_sdk_application_insights.types.os_type

        out["OsType"] = (
            aws_sdk_application_insights.types.os_type.serialize_aws_json_1_1(
                value["os_type"]
            )
        )
    if "tier" in value:
        import aws_sdk_application_insights.types.tier

        out["Tier"] = aws_sdk_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "monitor" in value:
        out["Monitor"] = value["monitor"]
    if "detected_workload" in value:
        import aws_sdk_application_insights.types.detected_workload

        out["DetectedWorkload"] = (
            aws_sdk_application_insights.types.detected_workload.serialize_aws_json_1_1(
                value["detected_workload"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationComponent:
    out: ApplicationComponent = {}  # type: ignore[typeddict-item]
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    if "ComponentRemarks" in data:
        out["component_remarks"] = data["ComponentRemarks"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "OsType" in data:
        import aws_sdk_application_insights.types.os_type

        out["os_type"] = (
            aws_sdk_application_insights.types.os_type.deserialize_aws_json_1_1(
                data["OsType"]
            )
        )
    if "Tier" in data:
        import aws_sdk_application_insights.types.tier

        out["tier"] = aws_sdk_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if "Monitor" in data:
        out["monitor"] = data["Monitor"]
    if "DetectedWorkload" in data:
        import aws_sdk_application_insights.types.detected_workload

        out["detected_workload"] = (
            aws_sdk_application_insights.types.detected_workload.deserialize_aws_json_1_1(
                data["DetectedWorkload"]
            )
        )
    return out
