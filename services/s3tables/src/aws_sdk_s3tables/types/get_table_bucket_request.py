"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn


class GetTableBucketRequest(TypedDict, closed=True):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableBucketRequest:
    out: GetTableBucketRequest = {}  # type: ignore[typeddict-item]
    return out
