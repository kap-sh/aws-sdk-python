"""Generated from Smithy shape ``com.amazonaws.s3tables#DeleteTableBucketMetricsConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn


class DeleteTableBucketMetricsConfigurationRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTableBucketMetricsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTableBucketMetricsConfigurationRequest:
    out: DeleteTableBucketMetricsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
