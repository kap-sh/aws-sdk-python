"""Generated from Smithy shape ``com.amazonaws.gamelift#LogConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.log_destination
    import aws_sdk_gamelift.types.log_group_arn_string_model
    import aws_sdk_gamelift.types.non_empty_string


class LogConfiguration(TypedDict):
    log_destination: NotRequired[
        "aws_sdk_gamelift.types.log_destination.LogDestination"
    ]
    """<p>The type of log collection to use for a fleet.</p> <ul> <li> <p> <code>CLOUDWATCH</code> -- (default value) Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group. </p> </li> <li> <p> <code>S3</code> -- Store logs in an Amazon S3 bucket that you define. This bucket must reside in the fleet's home Amazon Web Services Region.</p> </li> <li> <p> <code>NONE</code> -- Don't collect container logs.</p> </li> </ul>"""
    s3_bucket_name: NotRequired[
        "aws_sdk_gamelift.types.non_empty_string.NonEmptyString"
    ]
    """<p>If log destination is <code>S3</code>, logs are sent to the specified Amazon S3 bucket name.</p>"""
    log_group_arn: NotRequired[
        "aws_sdk_gamelift.types.log_group_arn_string_model.LogGroupArnStringModel"
    ]
    """<p>If log destination is <code>CLOUDWATCH</code>, logs are sent to the specified log group in Amazon CloudWatch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogConfiguration) -> dict:
    out: dict = {}
    if "log_destination" in value:
        import aws_sdk_gamelift.types.log_destination

        out["LogDestination"] = (
            aws_sdk_gamelift.types.log_destination.serialize_aws_json_1_1(
                value["log_destination"]
            )
        )
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if "LogDestination" in data:
        import aws_sdk_gamelift.types.log_destination

        out["log_destination"] = (
            aws_sdk_gamelift.types.log_destination.deserialize_aws_json_1_1(
                data["LogDestination"]
            )
        )
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
