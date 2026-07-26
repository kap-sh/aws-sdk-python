"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketMetricsConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn


class GetTableBucketMetricsConfigurationResponse(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    id: NotRequired["str"]
    """<p>The unique identifier of the metrics configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketMetricsConfigurationResponse) -> dict:
    out: dict = {}
    out["tableBucketARN"] = value["table_bucket_arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> GetTableBucketMetricsConfigurationResponse:
    out: GetTableBucketMetricsConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "tableBucketARN" in data:
        out["table_bucket_arn"] = data["tableBucketARN"]
    else:
        raise DeserializationError(
            "GetTableBucketMetricsConfigurationResponse.table_bucket_arn required"
        )
    if "id" in data:
        out["id"] = data["id"]
    return out
