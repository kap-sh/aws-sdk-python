"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FileFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.csv
    import capo_iotsitewise.types.parquet


class FileFormat(TypedDict, closed=True):
    csv: NotRequired["capo_iotsitewise.types.csv.Csv"]
    """<p>The file is in .CSV format.</p>"""
    parquet: NotRequired["capo_iotsitewise.types.parquet.Parquet"]
    """<p>The file is in parquet format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileFormat) -> dict:
    out: dict = {}
    if "csv" in value:
        import capo_iotsitewise.types.csv

        out["csv"] = capo_iotsitewise.types.csv.serialize_json(value["csv"])
    if "parquet" in value:
        import capo_iotsitewise.types.parquet

        out["parquet"] = capo_iotsitewise.types.parquet.serialize_json(value["parquet"])
    return out


def deserialize_json(data: dict) -> FileFormat:
    out: FileFormat = {}  # type: ignore[typeddict-item]
    if "csv" in data:
        import capo_iotsitewise.types.csv

        out["csv"] = capo_iotsitewise.types.csv.deserialize_json(data["csv"])
    if "parquet" in data:
        import capo_iotsitewise.types.parquet

        out["parquet"] = capo_iotsitewise.types.parquet.deserialize_json(
            data["parquet"]
        )
    return out
