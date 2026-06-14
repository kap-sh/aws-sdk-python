"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ErrorReportLocation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.bucket
    import aws_sdk_iotsitewise.types.string


class ErrorReportLocation(TypedDict):
    bucket: "aws_sdk_iotsitewise.types.bucket.Bucket"
    """<p>The name of the Amazon S3 bucket to which errors associated with the bulk import job are sent.</p>"""
    prefix: "aws_sdk_iotsitewise.types.string.String"
    r"""<p>Amazon S3 uses the prefix as a folder name to organize data in the bucket. Each Amazon S3 object has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/). For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html\">Organizing objects using prefixes</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorReportLocation) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ErrorReportLocation:
    out: ErrorReportLocation = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("ErrorReportLocation.bucket required")
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError("ErrorReportLocation.prefix required")
    return out
