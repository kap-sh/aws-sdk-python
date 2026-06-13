"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketMetricsConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn


class GetTableBucketMetricsConfigurationRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketMetricsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableBucketMetricsConfigurationRequest:
    out: GetTableBucketMetricsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
