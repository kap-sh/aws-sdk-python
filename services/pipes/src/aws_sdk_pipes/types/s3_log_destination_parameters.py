"""Generated from Smithy shape ``com.amazonaws.pipes#S3LogDestinationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.s3_output_format
    import aws_sdk_pipes.types.string


class S3LogDestinationParameters(TypedDict, closed=True):
    bucket_name: "aws_sdk_pipes.types.string.String"
    """<p>Specifies the name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.</p>"""
    bucket_owner: "aws_sdk_pipes.types.string.String"
    """<p>Specifies the Amazon Web Services account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.</p>"""
    output_format: NotRequired["aws_sdk_pipes.types.s3_output_format.S3OutputFormat"]
    """<p>How EventBridge should format the log records.</p> <p>EventBridge currently only supports <code>json</code> formatting.</p>"""
    prefix: NotRequired["aws_sdk_pipes.types.string.String"]
    r"""<p>Specifies any prefix text with which to begin Amazon S3 log object names.</p> <p>You can use prefixes to organize the data that you store in Amazon S3 buckets. A prefix is a string of characters at the beginning of the object key name. A prefix can be any length, subject to the maximum length of the object key name (1,024 bytes). For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html\">Organizing objects using prefixes</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3LogDestinationParameters) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["BucketOwner"] = value["bucket_owner"]
    if "output_format" in value:
        out["OutputFormat"] = value["output_format"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3LogDestinationParameters:
    out: S3LogDestinationParameters = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3LogDestinationParameters.bucket_name required")
    if "BucketOwner" in data:
        out["bucket_owner"] = data["BucketOwner"]
    else:
        raise DeserializationError("S3LogDestinationParameters.bucket_owner required")
    if "OutputFormat" in data:
        out["output_format"] = data["OutputFormat"]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    return out
