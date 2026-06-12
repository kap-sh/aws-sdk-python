"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketLoggingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketLoggingConfiguration(TypedDict):
    destination_bucket_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the S3 bucket where log files for the S3 bucket are stored.</p>"""
    log_file_prefix: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The prefix added to log files for the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketLoggingConfiguration) -> dict:
    out: dict = {}
    if "destination_bucket_name" in value:
        out["DestinationBucketName"] = value["destination_bucket_name"]
    if "log_file_prefix" in value:
        out["LogFilePrefix"] = value["log_file_prefix"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketLoggingConfiguration:
    out: AwsS3BucketLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "DestinationBucketName" in data:
        out["destination_bucket_name"] = data["DestinationBucketName"]
    if "LogFilePrefix" in data:
        out["log_file_prefix"] = data["LogFilePrefix"]
    return out
