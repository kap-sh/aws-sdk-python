"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketMetricsConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn


class PutTableBucketMetricsConfigurationRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketMetricsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutTableBucketMetricsConfigurationRequest:
    out: PutTableBucketMetricsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
