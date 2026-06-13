"""Generated from Smithy shape ``com.amazonaws.s3tables#DeleteTableBucketPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn


class DeleteTableBucketPolicyRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTableBucketPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTableBucketPolicyRequest:
    out: DeleteTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
