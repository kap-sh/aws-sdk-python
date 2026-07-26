"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergCompactionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_compaction_strategy
    import capo_s3tables.types.positive_integer


class IcebergCompactionSettings(TypedDict, closed=True):
    target_file_size_mb: NotRequired[
        "capo_s3tables.types.positive_integer.PositiveInteger"
    ]
    """<p>The target file size for the table in MB.</p>"""
    strategy: NotRequired[
        "capo_s3tables.types.iceberg_compaction_strategy.IcebergCompactionStrategy"
    ]
    """<p>The compaction strategy to use for the table. This determines how files are selected and combined during compaction operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergCompactionSettings) -> dict:
    out: dict = {}
    if "target_file_size_mb" in value:
        out["targetFileSizeMB"] = value["target_file_size_mb"]
    if "strategy" in value:
        import capo_s3tables.types.iceberg_compaction_strategy

        out["strategy"] = (
            capo_s3tables.types.iceberg_compaction_strategy.serialize_json(
                value["strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> IcebergCompactionSettings:
    out: IcebergCompactionSettings = {}  # type: ignore[typeddict-item]
    if "targetFileSizeMB" in data:
        out["target_file_size_mb"] = data["targetFileSizeMB"]
    if "strategy" in data:
        import capo_s3tables.types.iceberg_compaction_strategy

        out["strategy"] = (
            capo_s3tables.types.iceberg_compaction_strategy.deserialize_json(
                data["strategy"]
            )
        )
    return out
