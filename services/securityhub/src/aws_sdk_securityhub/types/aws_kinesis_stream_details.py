"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsKinesisStreamDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_kinesis_stream_stream_encryption_details
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsKinesisStreamDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Kinesis stream. If you don't specify a name, CloudFront generates a unique physical ID and uses that ID for the stream name. </p>"""
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the Kinesis data stream. </p>"""
    stream_encryption: NotRequired[
        "aws_sdk_securityhub.types.aws_kinesis_stream_stream_encryption_details.AwsKinesisStreamStreamEncryptionDetails"
    ]
    """<p>When specified, enables or updates server-side encryption using an KMS key for a specified stream. Removing this property from your stack template and updating your stack disables encryption. </p>"""
    shard_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of shards that the stream uses. </p>"""
    retention_period_hours: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of hours for the data records that are stored in shards to remain accessible. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsKinesisStreamDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "stream_encryption" in value:
        import aws_sdk_securityhub.types.aws_kinesis_stream_stream_encryption_details

        out["StreamEncryption"] = (
            aws_sdk_securityhub.types.aws_kinesis_stream_stream_encryption_details.serialize_json(
                value["stream_encryption"]
            )
        )
    if "shard_count" in value:
        out["ShardCount"] = value["shard_count"]
    if "retention_period_hours" in value:
        out["RetentionPeriodHours"] = value["retention_period_hours"]
    return out


def deserialize_json(data: dict) -> AwsKinesisStreamDetails:
    out: AwsKinesisStreamDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "StreamEncryption" in data:
        import aws_sdk_securityhub.types.aws_kinesis_stream_stream_encryption_details

        out["stream_encryption"] = (
            aws_sdk_securityhub.types.aws_kinesis_stream_stream_encryption_details.deserialize_json(
                data["StreamEncryption"]
            )
        )
    if "ShardCount" in data:
        out["shard_count"] = data["ShardCount"]
    if "RetentionPeriodHours" in data:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    return out
