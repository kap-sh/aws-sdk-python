"""Generated from Smithy shape ``com.amazonaws.fsx#LustreLogCreateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.general_arn
    import aws_sdk_fsx.types.lustre_access_audit_log_level


class LustreLogCreateConfiguration(TypedDict):
    level: NotRequired[
        "aws_sdk_fsx.types.lustre_access_audit_log_level.LustreAccessAuditLogLevel"
    ]
    """<p>Sets which data repository events are logged by Amazon FSx.</p> <ul> <li> <p> <code>WARN_ONLY</code> - only warning events are logged.</p> </li> <li> <p> <code>ERROR_ONLY</code> - only error events are logged.</p> </li> <li> <p> <code>WARN_ERROR</code> - both warning events and error events are logged.</p> </li> <li> <p> <code>DISABLED</code> - logging of data repository events is turned off.</p> </li> </ul>"""
    destination: NotRequired["aws_sdk_fsx.types.general_arn.GeneralARN"]
    """<p>The Amazon Resource Name (ARN) that specifies the destination of the logs.</p> <p>The destination can be any Amazon CloudWatch Logs log group ARN, with the following requirements:</p> <ul> <li> <p>The destination ARN that you provide must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.</p> </li> <li> <p>The name of the Amazon CloudWatch Logs log group must begin with the <code>/aws/fsx</code> prefix.</p> </li> <li> <p>If you do not provide a destination, Amazon FSx will create and use a log stream in the CloudWatch Logs <code>/aws/fsx/lustre</code> log group (for Amazon FSx for Lustre) or <code>/aws/fsx/filecache</code> (for Amazon File Cache).</p> </li> <li> <p>If <code>Destination</code> is provided and the resource does not exist, the request will fail with a <code>BadRequest</code> error.</p> </li> <li> <p>If <code>Level</code> is set to <code>DISABLED</code>, you cannot specify a destination in <code>Destination</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreLogCreateConfiguration) -> dict:
    out: dict = {}
    if "level" in value:
        import aws_sdk_fsx.types.lustre_access_audit_log_level

        out["Level"] = (
            aws_sdk_fsx.types.lustre_access_audit_log_level.serialize_aws_json_1_1(
                value["level"]
            )
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LustreLogCreateConfiguration:
    out: LustreLogCreateConfiguration = {}  # type: ignore[typeddict-item]
    if "Level" in data:
        import aws_sdk_fsx.types.lustre_access_audit_log_level

        out["level"] = (
            aws_sdk_fsx.types.lustre_access_audit_log_level.deserialize_aws_json_1_1(
                data["Level"]
            )
        )
    if "Destination" in data:
        out["destination"] = data["Destination"]
    return out
