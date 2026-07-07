"""Generated from Smithy shape ``com.amazonaws.glue#OrphanFileDeletionMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_orphan_file_deletion_metrics


class OrphanFileDeletionMetrics(TypedDict, closed=True):
    iceberg_metrics: NotRequired[
        "aws_sdk_glue.types.iceberg_orphan_file_deletion_metrics.IcebergOrphanFileDeletionMetrics"
    ]
    """<p>A structure containing the Iceberg orphan file deletion metrics for the optimizer run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrphanFileDeletionMetrics) -> dict:
    out: dict = {}
    if "iceberg_metrics" in value:
        import aws_sdk_glue.types.iceberg_orphan_file_deletion_metrics

        out["IcebergMetrics"] = (
            aws_sdk_glue.types.iceberg_orphan_file_deletion_metrics.serialize_aws_json_1_1(
                value["iceberg_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrphanFileDeletionMetrics:
    out: OrphanFileDeletionMetrics = {}  # type: ignore[typeddict-item]
    if "IcebergMetrics" in data:
        import aws_sdk_glue.types.iceberg_orphan_file_deletion_metrics

        out["iceberg_metrics"] = (
            aws_sdk_glue.types.iceberg_orphan_file_deletion_metrics.deserialize_aws_json_1_1(
                data["IcebergMetrics"]
            )
        )
    return out
