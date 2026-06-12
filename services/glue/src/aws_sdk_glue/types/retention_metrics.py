"""Generated from Smithy shape ``com.amazonaws.glue#RetentionMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_retention_metrics


class RetentionMetrics(TypedDict):
    iceberg_metrics: NotRequired[
        "aws_sdk_glue.types.iceberg_retention_metrics.IcebergRetentionMetrics"
    ]
    """<p>A structure containing the Iceberg retention metrics for the optimizer run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionMetrics) -> dict:
    out: dict = {}
    if "iceberg_metrics" in value:
        import aws_sdk_glue.types.iceberg_retention_metrics

        out["IcebergMetrics"] = (
            aws_sdk_glue.types.iceberg_retention_metrics.serialize_aws_json_1_1(
                value["iceberg_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetentionMetrics:
    out: RetentionMetrics = {}  # type: ignore[typeddict-item]
    if "IcebergMetrics" in data:
        import aws_sdk_glue.types.iceberg_retention_metrics

        out["iceberg_metrics"] = (
            aws_sdk_glue.types.iceberg_retention_metrics.deserialize_aws_json_1_1(
                data["IcebergMetrics"]
            )
        )
    return out
