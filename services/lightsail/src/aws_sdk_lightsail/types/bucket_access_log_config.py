"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketAccessLogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.bucket_access_log_prefix
    import aws_sdk_lightsail.types.bucket_name


class BucketAccessLogConfig(TypedDict, closed=True):
    enabled: "aws_sdk_lightsail.types.boolean.boolean"
    """<p>A Boolean value that indicates whether bucket access logging is enabled for the bucket.</p>"""
    destination: NotRequired["aws_sdk_lightsail.types.bucket_name.BucketName"]
    """<p>The name of the bucket where the access logs are saved. The destination can be a Lightsail bucket in the same account, and in the same Amazon Web Services Region as the source bucket.</p> <note> <p>This parameter is required when enabling the access log for a bucket, and should be omitted when disabling the access log.</p> </note>"""
    prefix: NotRequired[
        "aws_sdk_lightsail.types.bucket_access_log_prefix.BucketAccessLogPrefix"
    ]
    """<p>The optional object prefix for the bucket access log.</p> <p>The prefix is an optional addition to the object key that organizes your access log files in the destination bucket. For example, if you specify a <code>logs/</code> prefix, then each log object will begin with the <code>logs/</code> prefix in its key (for example, <code>logs/2021-11-01-21-32-16-E568B2907131C0C0</code>).</p> <note> <p>This parameter can be optionally specified when enabling the access log for a bucket, and should be omitted when disabling the access log.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketAccessLogConfig) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "destination" in value:
        out["destination"] = value["destination"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BucketAccessLogConfig:
    out: BucketAccessLogConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("BucketAccessLogConfig.enabled required")
    if "destination" in data:
        out["destination"] = data["destination"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
