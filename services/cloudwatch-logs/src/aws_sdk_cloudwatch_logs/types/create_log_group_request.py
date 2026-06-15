"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLogGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.deletion_protection_enabled
    import aws_sdk_cloudwatch_logs.types.kms_key_id
    import aws_sdk_cloudwatch_logs.types.log_group_class
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.tags


class CreateLogGroupRequest(TypedDict):
    log_group_name: "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>A name for the log group.</p>"""
    kms_key_id: NotRequired["aws_sdk_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    r"""<p>The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms\">Amazon Resource Names</a>.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    r"""<p>The key-value pairs to use for the tags.</p> <p>You can grant users access to certain log groups while preventing them from accessing other log groups. To do so, tag your groups and use IAM policies that refer to those tags. To assign tags when you create a log group, you must have either the <code>logs:TagResource</code> or <code>logs:TagLogGroup</code> permission. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a>. For more information about using tags to control access, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Controlling access to Amazon Web Services resources using tags</a>.</p>"""
    log_group_class: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_class.LogGroupClass"
    ]
    r"""<p>Use this parameter to specify the log group class for this log group. There are three classes:</p> <ul> <li> <p>The <code>Standard</code> log class supports all CloudWatch Logs features.</p> </li> <li> <p>The <code>Infrequent Access</code> log class supports a subset of CloudWatch Logs features and incurs lower costs.</p> </li> <li> <p>Use the <code>Delivery</code> log class only for delivering Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.</p> </li> </ul> <p>If you omit this parameter, the default of <code>STANDARD</code> is used.</p> <important> <p>The value of <code>logGroupClass</code> can't be changed after a log group is created.</p> </important> <p>For details about the features supported by each class, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html\">Log classes</a> </p>"""
    deletion_protection_enabled: NotRequired[
        "aws_sdk_cloudwatch_logs.types.deletion_protection_enabled.DeletionProtectionEnabled"
    ]
    """<p>Use this parameter to enable deletion protection for the new log group. When enabled on a log group, deletion protection blocks all deletion operations until it is explicitly disabled. By default log groups are created without deletion protection enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogGroupRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "log_group_class" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["logGroupClass"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.serialize_aws_json_1_1(
                value["log_group_class"]
            )
        )
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogGroupRequest:
    out: CreateLogGroupRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("CreateLogGroupRequest.log_group_name required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "logGroupClass" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["log_group_class"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.deserialize_aws_json_1_1(
                data["logGroupClass"]
            )
        )
    if "deletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    return out
