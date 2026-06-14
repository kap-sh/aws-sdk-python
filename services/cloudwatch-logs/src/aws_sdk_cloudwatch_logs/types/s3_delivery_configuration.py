"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3DeliveryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.boolean
    import aws_sdk_cloudwatch_logs.types.delivery_suffix_path


class S3DeliveryConfiguration(TypedDict):
    suffix_path: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_suffix_path.DeliverySuffixPath"
    ]
    """<p>This string allows re-configuring the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path will vary by each log source. To find the values supported for the suffix path for each log source, use the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html\">DescribeConfigurationTemplates</a> operation and check the <code>allowedSuffixPathFields</code> field in the response.</p>"""
    enable_hive_compatible_path: NotRequired[
        "aws_sdk_cloudwatch_logs.types.boolean.Boolean"
    ]
    """<p>This parameter causes the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DeliveryConfiguration) -> dict:
    out: dict = {}
    if "suffix_path" in value:
        out["suffixPath"] = value["suffix_path"]
    if "enable_hive_compatible_path" in value:
        out["enableHiveCompatiblePath"] = value["enable_hive_compatible_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DeliveryConfiguration:
    out: S3DeliveryConfiguration = {}  # type: ignore[typeddict-item]
    if "suffixPath" in data:
        out["suffix_path"] = data["suffixPath"]
    if "enableHiveCompatiblePath" in data:
        out["enable_hive_compatible_path"] = data["enableHiveCompatiblePath"]
    return out
