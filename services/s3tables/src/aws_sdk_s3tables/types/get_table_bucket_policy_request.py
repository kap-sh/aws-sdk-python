"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn


class GetTableBucketPolicyRequest(TypedDict, closed=True):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableBucketPolicyRequest:
    out: GetTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
