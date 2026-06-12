"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerAccessLog``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbLoadBalancerAccessLog(TypedDict):
    emit_interval: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The interval in minutes for publishing the access logs.</p> <p>You can publish access logs either every 5 minutes or every 60 minutes.</p>"""
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether access logs are enabled for the load balancer.</p>"""
    s3_bucket_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the S3 bucket where the access logs are stored.</p>"""
    s3_bucket_prefix: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The logical hierarchy that was created for the S3 bucket.</p> <p>If a prefix is not provided, the log is placed at the root level of the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerAccessLog) -> dict:
    out: dict = {}
    if "emit_interval" in value:
        out["EmitInterval"] = value["emit_interval"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_bucket_prefix" in value:
        out["S3BucketPrefix"] = value["s3_bucket_prefix"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerAccessLog:
    out: AwsElbLoadBalancerAccessLog = {}  # type: ignore[typeddict-item]
    if "EmitInterval" in data:
        out["emit_interval"] = data["EmitInterval"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3BucketPrefix" in data:
        out["s3_bucket_prefix"] = data["S3BucketPrefix"]
    return out
