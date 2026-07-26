"""Generated from Smithy shape ``com.amazonaws.backup#ReportPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.report_delivery_channel
    import capo_backup.types.report_plan_description
    import capo_backup.types.report_plan_name
    import capo_backup.types.report_setting
    import capo_backup.types.string
    import capo_backup.types.timestamp


class ReportPlan(TypedDict, closed=True):
    report_plan_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    report_plan_name: NotRequired["capo_backup.types.report_plan_name.ReportPlanName"]
    """<p>The unique name of the report plan. This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    report_plan_description: NotRequired[
        "capo_backup.types.report_plan_description.ReportPlanDescription"
    ]
    """<p>An optional description of the report plan with a maximum 1,024 characters.</p>"""
    report_setting: NotRequired["capo_backup.types.report_setting.ReportSetting"]
    """<p>Identifies the report template for the report. Reports are built using a report template. The report templates are:</p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT</code> </p> <p>If the report template is <code>RESOURCE_COMPLIANCE_REPORT</code> or <code>CONTROL_COMPLIANCE_REPORT</code>, this API resource also describes the report coverage by Amazon Web Services Regions and frameworks.</p>"""
    report_delivery_channel: NotRequired[
        "capo_backup.types.report_delivery_channel.ReportDeliveryChannel"
    ]
    """<p>Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.</p>"""
    deployment_status: NotRequired["capo_backup.types.string.string"]
    """<p>The deployment status of a report plan. The statuses are:</p> <p> <code>CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED</code> </p>"""
    creation_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a report plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    last_attempted_execution_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a report job associated with this report plan last attempted to run, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastAttemptedExecutionTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    last_successful_execution_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a report job associated with this report plan last successfully ran, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastSuccessfulExecutionTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportPlan) -> dict:
    out: dict = {}
    if "report_plan_arn" in value:
        out["ReportPlanArn"] = value["report_plan_arn"]
    if "report_plan_name" in value:
        out["ReportPlanName"] = value["report_plan_name"]
    if "report_plan_description" in value:
        out["ReportPlanDescription"] = value["report_plan_description"]
    if "report_setting" in value:
        import capo_backup.types.report_setting

        out["ReportSetting"] = capo_backup.types.report_setting.serialize_json(
            value["report_setting"]
        )
    if "report_delivery_channel" in value:
        import capo_backup.types.report_delivery_channel

        out["ReportDeliveryChannel"] = (
            capo_backup.types.report_delivery_channel.serialize_json(
                value["report_delivery_channel"]
            )
        )
    if "deployment_status" in value:
        out["DeploymentStatus"] = value["deployment_status"]
    if "creation_time" in value:
        import capo_backup.types.timestamp

        out["CreationTime"] = capo_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_attempted_execution_time" in value:
        import capo_backup.types.timestamp

        out["LastAttemptedExecutionTime"] = capo_backup.types.timestamp.serialize_json(
            value["last_attempted_execution_time"]
        )
    if "last_successful_execution_time" in value:
        import capo_backup.types.timestamp

        out["LastSuccessfulExecutionTime"] = capo_backup.types.timestamp.serialize_json(
            value["last_successful_execution_time"]
        )
    return out


def deserialize_json(data: dict) -> ReportPlan:
    out: ReportPlan = {}  # type: ignore[typeddict-item]
    if "ReportPlanArn" in data:
        out["report_plan_arn"] = data["ReportPlanArn"]
    if "ReportPlanName" in data:
        out["report_plan_name"] = data["ReportPlanName"]
    if "ReportPlanDescription" in data:
        out["report_plan_description"] = data["ReportPlanDescription"]
    if "ReportSetting" in data:
        import capo_backup.types.report_setting

        out["report_setting"] = capo_backup.types.report_setting.deserialize_json(
            data["ReportSetting"]
        )
    if "ReportDeliveryChannel" in data:
        import capo_backup.types.report_delivery_channel

        out["report_delivery_channel"] = (
            capo_backup.types.report_delivery_channel.deserialize_json(
                data["ReportDeliveryChannel"]
            )
        )
    if "DeploymentStatus" in data:
        out["deployment_status"] = data["DeploymentStatus"]
    if "CreationTime" in data:
        import capo_backup.types.timestamp

        out["creation_time"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "LastAttemptedExecutionTime" in data:
        import capo_backup.types.timestamp

        out["last_attempted_execution_time"] = (
            capo_backup.types.timestamp.deserialize_json(
                data["LastAttemptedExecutionTime"]
            )
        )
    if "LastSuccessfulExecutionTime" in data:
        import capo_backup.types.timestamp

        out["last_successful_execution_time"] = (
            capo_backup.types.timestamp.deserialize_json(
                data["LastSuccessfulExecutionTime"]
            )
        )
    return out
