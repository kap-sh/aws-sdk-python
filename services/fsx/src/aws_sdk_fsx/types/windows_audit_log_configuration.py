"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsAuditLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.general_arn
    import aws_sdk_fsx.types.windows_access_audit_log_level


class WindowsAuditLogConfiguration(TypedDict, closed=True):
    file_access_audit_log_level: NotRequired[
        "aws_sdk_fsx.types.windows_access_audit_log_level.WindowsAccessAuditLogLevel"
    ]
    """<p>Sets which attempt type is logged by Amazon FSx for file and folder accesses.</p> <ul> <li> <p> <code>SUCCESS_ONLY</code> - only successful attempts to access files or folders are logged.</p> </li> <li> <p> <code>FAILURE_ONLY</code> - only failed attempts to access files or folders are logged.</p> </li> <li> <p> <code>SUCCESS_AND_FAILURE</code> - both successful attempts and failed attempts to access files or folders are logged.</p> </li> <li> <p> <code>DISABLED</code> - access auditing of files and folders is turned off.</p> </li> </ul>"""
    file_share_access_audit_log_level: NotRequired[
        "aws_sdk_fsx.types.windows_access_audit_log_level.WindowsAccessAuditLogLevel"
    ]
    """<p>Sets which attempt type is logged by Amazon FSx for file share accesses.</p> <ul> <li> <p> <code>SUCCESS_ONLY</code> - only successful attempts to access file shares are logged.</p> </li> <li> <p> <code>FAILURE_ONLY</code> - only failed attempts to access file shares are logged.</p> </li> <li> <p> <code>SUCCESS_AND_FAILURE</code> - both successful attempts and failed attempts to access file shares are logged.</p> </li> <li> <p> <code>DISABLED</code> - access auditing of file shares is turned off.</p> </li> </ul>"""
    audit_log_destination: NotRequired["aws_sdk_fsx.types.general_arn.GeneralARN"]
    """<p>The Amazon Resource Name (ARN) for the destination of the audit logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.</p> <p>The name of the Amazon CloudWatch Logs log group must begin with the <code>/aws/fsx</code> prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the <code>aws-fsx</code> prefix.</p> <p>The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowsAuditLogConfiguration) -> dict:
    out: dict = {}
    if "file_access_audit_log_level" in value:
        import aws_sdk_fsx.types.windows_access_audit_log_level

        out["FileAccessAuditLogLevel"] = (
            aws_sdk_fsx.types.windows_access_audit_log_level.serialize_aws_json_1_1(
                value["file_access_audit_log_level"]
            )
        )
    if "file_share_access_audit_log_level" in value:
        import aws_sdk_fsx.types.windows_access_audit_log_level

        out["FileShareAccessAuditLogLevel"] = (
            aws_sdk_fsx.types.windows_access_audit_log_level.serialize_aws_json_1_1(
                value["file_share_access_audit_log_level"]
            )
        )
    if "audit_log_destination" in value:
        out["AuditLogDestination"] = value["audit_log_destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WindowsAuditLogConfiguration:
    out: WindowsAuditLogConfiguration = {}  # type: ignore[typeddict-item]
    if "FileAccessAuditLogLevel" in data:
        import aws_sdk_fsx.types.windows_access_audit_log_level

        out["file_access_audit_log_level"] = (
            aws_sdk_fsx.types.windows_access_audit_log_level.deserialize_aws_json_1_1(
                data["FileAccessAuditLogLevel"]
            )
        )
    if "FileShareAccessAuditLogLevel" in data:
        import aws_sdk_fsx.types.windows_access_audit_log_level

        out["file_share_access_audit_log_level"] = (
            aws_sdk_fsx.types.windows_access_audit_log_level.deserialize_aws_json_1_1(
                data["FileShareAccessAuditLogLevel"]
            )
        )
    if "AuditLogDestination" in data:
        out["audit_log_destination"] = data["AuditLogDestination"]
    return out
