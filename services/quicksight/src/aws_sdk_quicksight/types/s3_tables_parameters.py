"""Generated from Smithy shape ``com.amazonaws.quicksight#S3TablesParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.s3_table_bucket_arn


class S3TablesParameters(TypedDict, closed=True):
    table_bucket_arn: NotRequired[
        "aws_sdk_quicksight.types.s3_table_bucket_arn.S3TableBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 Tables bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3TablesParameters) -> dict:
    out: dict = {}
    if "table_bucket_arn" in value:
        out["TableBucketArn"] = value["table_bucket_arn"]
    return out


def deserialize_json(data: dict) -> S3TablesParameters:
    out: S3TablesParameters = {}  # type: ignore[typeddict-item]
    if "TableBucketArn" in data:
        out["table_bucket_arn"] = data["TableBucketArn"]
    return out
