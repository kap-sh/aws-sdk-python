"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateAcceleratorAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_boolean
    import aws_sdk_global_accelerator.types.generic_string


class UpdateAcceleratorAttributesRequest(TypedDict):
    accelerator_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the accelerator that you want to update.</p>"""
    flow_logs_enabled: NotRequired[
        "aws_sdk_global_accelerator.types.generic_boolean.GenericBoolean"
    ]
    r"""<p>Update whether flow logs are enabled. The default value is false. If the value is true, <code>FlowLogsS3Bucket</code> and <code>FlowLogsS3Prefix</code> must be specified.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html\">Flow Logs</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""
    flow_logs_s3_bucket: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The name of the Amazon S3 bucket for the flow logs. Attribute is required if <code>FlowLogsEnabled</code> is <code>true</code>. The bucket must exist and have a bucket policy that grants Global Accelerator permission to write to the bucket.</p>"""
    flow_logs_s3_prefix: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>Update the prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if <code>FlowLogsEnabled</code> is <code>true</code>. </p> <p>If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:</p> <p>s3-bucket_name//AWSLogs/aws_account_id</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAcceleratorAttributesRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    if "flow_logs_enabled" in value:
        out["FlowLogsEnabled"] = value["flow_logs_enabled"]
    if "flow_logs_s3_bucket" in value:
        out["FlowLogsS3Bucket"] = value["flow_logs_s3_bucket"]
    if "flow_logs_s3_prefix" in value:
        out["FlowLogsS3Prefix"] = value["flow_logs_s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAcceleratorAttributesRequest:
    out: UpdateAcceleratorAttributesRequest = {}  # type: ignore[typeddict-item]
    if "AcceleratorArn" in data:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        raise DeserializationError(
            "UpdateAcceleratorAttributesRequest.accelerator_arn required"
        )
    if "FlowLogsEnabled" in data:
        out["flow_logs_enabled"] = data["FlowLogsEnabled"]
    if "FlowLogsS3Bucket" in data:
        out["flow_logs_s3_bucket"] = data["FlowLogsS3Bucket"]
    if "FlowLogsS3Prefix" in data:
        out["flow_logs_s3_prefix"] = data["FlowLogsS3Prefix"]
    return out
