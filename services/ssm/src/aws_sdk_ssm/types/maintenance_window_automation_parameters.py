"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowAutomationParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_parameter_map
    import aws_sdk_ssm.types.document_version


class MaintenanceWindowAutomationParameters(TypedDict):
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of an Automation runbook to use during task execution.</p>"""
    parameters: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The parameters for the <code>AUTOMATION</code> task.</p> <p>For information about specifying and updating task parameters, see <a>RegisterTaskWithMaintenanceWindow</a> and <a>UpdateMaintenanceWindowTask</a>.</p> <note> <p> <code>LoggingInfo</code> has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the <code>OutputS3BucketName</code> and <code>OutputS3KeyPrefix</code> options in the <code>TaskInvocationParameters</code> structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> <p>For <code>AUTOMATION</code> task types, Amazon Web Services Systems Manager ignores any values specified for these parameters.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowAutomationParameters) -> dict:
    out: dict = {}
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "parameters" in value:
        import aws_sdk_ssm.types.automation_parameter_map

        out["Parameters"] = (
            aws_sdk_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowAutomationParameters:
    out: MaintenanceWindowAutomationParameters = {}  # type: ignore[typeddict-item]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "Parameters" in data:
        import aws_sdk_ssm.types.automation_parameter_map

        out["parameters"] = (
            aws_sdk_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
