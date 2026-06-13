"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketStorageClassRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn


class GetTableBucketStorageClassRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketStorageClassRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableBucketStorageClassRequest:
    out: GetTableBucketStorageClassRequest = {}  # type: ignore[typeddict-item]
    return out
