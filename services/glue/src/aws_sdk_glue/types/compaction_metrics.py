"""Generated from Smithy shape ``com.amazonaws.glue#CompactionMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_compaction_metrics


class CompactionMetrics(TypedDict):
    iceberg_metrics: NotRequired[
        "aws_sdk_glue.types.iceberg_compaction_metrics.IcebergCompactionMetrics"
    ]
    """<p>A structure containing the Iceberg compaction metrics for the optimizer run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompactionMetrics) -> dict:
    out: dict = {}
    if "iceberg_metrics" in value:
        import aws_sdk_glue.types.iceberg_compaction_metrics

        out["IcebergMetrics"] = (
            aws_sdk_glue.types.iceberg_compaction_metrics.serialize_aws_json_1_1(
                value["iceberg_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompactionMetrics:
    out: CompactionMetrics = {}  # type: ignore[typeddict-item]
    if "IcebergMetrics" in data:
        import aws_sdk_glue.types.iceberg_compaction_metrics

        out["iceberg_metrics"] = (
            aws_sdk_glue.types.iceberg_compaction_metrics.deserialize_aws_json_1_1(
                data["IcebergMetrics"]
            )
        )
    return out
