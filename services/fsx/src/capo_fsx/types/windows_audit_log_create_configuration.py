"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsAuditLogCreateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.general_arn
    import capo_fsx.types.windows_access_audit_log_level


class WindowsAuditLogCreateConfiguration(TypedDict, closed=True):
    file_access_audit_log_level: NotRequired[
        "capo_fsx.types.windows_access_audit_log_level.WindowsAccessAuditLogLevel"
    ]
    """<p>Sets which attempt type is logged by Amazon FSx for file and folder accesses.</p> <ul> <li> <p> <code>SUCCESS_ONLY</code> - only successful attempts to access files or folders are logged.</p> </li> <li> <p> <code>FAILURE_ONLY</code> - only failed attempts to access files or folders are logged.</p> </li> <li> <p> <code>SUCCESS_AND_FAILURE</code> - both successful attempts and failed attempts to access files or folders are logged.</p> </li> <li> <p> <code>DISABLED</code> - access auditing of files and folders is turned off.</p> </li> </ul>"""
    file_share_access_audit_log_level: NotRequired[
        "capo_fsx.types.windows_access_audit_log_level.WindowsAccessAuditLogLevel"
    ]
    """<p>Sets which attempt type is logged by Amazon FSx for file share accesses.</p> <ul> <li> <p> <code>SUCCESS_ONLY</code> - only successful attempts to access file shares are logged.</p> </li> <li> <p> <code>FAILURE_ONLY</code> - only failed attempts to access file shares are logged.</p> </li> <li> <p> <code>SUCCESS_AND_FAILURE</code> - both successful attempts and failed attempts to access file shares are logged.</p> </li> <li> <p> <code>DISABLED</code> - access auditing of file shares is turned off.</p> </li> </ul>"""
    audit_log_destination: NotRequired["capo_fsx.types.general_arn.GeneralARN"]
    """<p>The Amazon Resource Name (ARN) that specifies the destination of the audit logs.</p> <p>The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN, with the following requirements:</p> <ul> <li> <p>The destination ARN that you provide (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.</p> </li> <li> <p>The name of the Amazon CloudWatch Logs log group must begin with the <code>/aws/fsx</code> prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the <code>aws-fsx</code> prefix.</p> </li> <li> <p>If you do not provide a destination in <code>AuditLogDestination</code>, Amazon FSx will create and use a log stream in the CloudWatch Logs <code>/aws/fsx/windows</code> log group.</p> </li> <li> <p>If <code>AuditLogDestination</code> is provided and the resource does not exist, the request will fail with a <code>BadRequest</code> error.</p> </li> <li> <p>If <code>FileAccessAuditLogLevel</code> and <code>FileShareAccessAuditLogLevel</code> are both set to <code>DISABLED</code>, you cannot specify a destination in <code>AuditLogDestination</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowsAuditLogCreateConfiguration) -> dict:
    out: dict = {}
    if "file_access_audit_log_level" in value:
        import capo_fsx.types.windows_access_audit_log_level

        out["FileAccessAuditLogLevel"] = (
            capo_fsx.types.windows_access_audit_log_level.serialize_aws_json_1_1(
                value["file_access_audit_log_level"]
            )
        )
    if "file_share_access_audit_log_level" in value:
        import capo_fsx.types.windows_access_audit_log_level

        out["FileShareAccessAuditLogLevel"] = (
            capo_fsx.types.windows_access_audit_log_level.serialize_aws_json_1_1(
                value["file_share_access_audit_log_level"]
            )
        )
    if "audit_log_destination" in value:
        out["AuditLogDestination"] = value["audit_log_destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WindowsAuditLogCreateConfiguration:
    out: WindowsAuditLogCreateConfiguration = {}  # type: ignore[typeddict-item]
    if "FileAccessAuditLogLevel" in data:
        import capo_fsx.types.windows_access_audit_log_level

        out["file_access_audit_log_level"] = (
            capo_fsx.types.windows_access_audit_log_level.deserialize_aws_json_1_1(
                data["FileAccessAuditLogLevel"]
            )
        )
    if "FileShareAccessAuditLogLevel" in data:
        import capo_fsx.types.windows_access_audit_log_level

        out["file_share_access_audit_log_level"] = (
            capo_fsx.types.windows_access_audit_log_level.deserialize_aws_json_1_1(
                data["FileShareAccessAuditLogLevel"]
            )
        )
    if "AuditLogDestination" in data:
        out["audit_log_destination"] = data["AuditLogDestination"]
    return out
