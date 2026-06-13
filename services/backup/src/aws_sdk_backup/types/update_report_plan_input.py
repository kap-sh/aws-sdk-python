"""Generated from Smithy shape ``com.amazonaws.backup#UpdateReportPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_delivery_channel
    import aws_sdk_backup.types.report_plan_description
    import aws_sdk_backup.types.report_plan_name
    import aws_sdk_backup.types.report_setting
    import aws_sdk_backup.types.string


class UpdateReportPlanInput(TypedDict):
    report_plan_name: "aws_sdk_backup.types.report_plan_name.ReportPlanName"
    """<p>The unique name of the report plan. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    report_plan_description: NotRequired[
        "aws_sdk_backup.types.report_plan_description.ReportPlanDescription"
    ]
    """<p>An optional description of the report plan with a maximum 1,024 characters.</p>"""
    report_delivery_channel: NotRequired[
        "aws_sdk_backup.types.report_delivery_channel.ReportDeliveryChannel"
    ]
    """<p>The information about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.</p>"""
    report_setting: NotRequired["aws_sdk_backup.types.report_setting.ReportSetting"]
    """<p>The report template for the report. Reports are built using a report template. The report templates are:</p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT</code> </p> <p>If the report template is <code>RESOURCE_COMPLIANCE_REPORT</code> or <code>CONTROL_COMPLIANCE_REPORT</code>, this API resource also describes the report coverage by Amazon Web Services Regions and frameworks.</p>"""
    idempotency_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>UpdateReportPlanInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReportPlanInput) -> dict:
    out: dict = {}
    if "report_plan_description" in value:
        out["ReportPlanDescription"] = value["report_plan_description"]
    if "report_delivery_channel" in value:
        import aws_sdk_backup.types.report_delivery_channel

        out["ReportDeliveryChannel"] = (
            aws_sdk_backup.types.report_delivery_channel.serialize_json(
                value["report_delivery_channel"]
            )
        )
    if "report_setting" in value:
        import aws_sdk_backup.types.report_setting

        out["ReportSetting"] = aws_sdk_backup.types.report_setting.serialize_json(
            value["report_setting"]
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_json(data: dict) -> UpdateReportPlanInput:
    out: UpdateReportPlanInput = {}  # type: ignore[typeddict-item]
    if "ReportPlanDescription" in data:
        out["report_plan_description"] = data["ReportPlanDescription"]
    if "ReportDeliveryChannel" in data:
        import aws_sdk_backup.types.report_delivery_channel

        out["report_delivery_channel"] = (
            aws_sdk_backup.types.report_delivery_channel.deserialize_json(
                data["ReportDeliveryChannel"]
            )
        )
    if "ReportSetting" in data:
        import aws_sdk_backup.types.report_setting

        out["report_setting"] = aws_sdk_backup.types.report_setting.deserialize_json(
            data["ReportSetting"]
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
