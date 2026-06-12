"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsFsrmConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.general_arn


class WindowsFsrmConfiguration(TypedDict):
    fsrm_service_enabled: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>Specifies whether FSRM is enabled or disabled on the file system. When <code>TRUE</code>, the FSRM service is enabled and monitor file operations according to configured policies. When <code>FALSE</code> or omitted, FSRM is disabled. The default value is <code>FALSE</code>. </p>"""
    event_log_destination: NotRequired["aws_sdk_fsx.types.general_arn.GeneralARN"]
    """<p>The Amazon Resource Name (ARN) for the destination of the FSRM event logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.</p> <p>The name of the Amazon CloudWatch Logs log group must begin with the <code>/aws/fsx</code> prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the <code>aws-fsx</code> prefix.</p> <p>The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowsFsrmConfiguration) -> dict:
    out: dict = {}
    if "fsrm_service_enabled" in value:
        out["FsrmServiceEnabled"] = value["fsrm_service_enabled"]
    if "event_log_destination" in value:
        out["EventLogDestination"] = value["event_log_destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WindowsFsrmConfiguration:
    out: WindowsFsrmConfiguration = {}  # type: ignore[typeddict-item]
    if "FsrmServiceEnabled" in data:
        out["fsrm_service_enabled"] = data["FsrmServiceEnabled"]
    if "EventLogDestination" in data:
        out["event_log_destination"] = data["EventLogDestination"]
    return out
