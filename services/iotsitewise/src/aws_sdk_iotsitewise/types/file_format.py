"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FileFormat``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.csv
    import aws_sdk_iotsitewise.types.parquet


class FileFormat(TypedDict):
    csv: NotRequired["aws_sdk_iotsitewise.types.csv.Csv"]
    """<p>The file is in .CSV format.</p>"""
    parquet: NotRequired["aws_sdk_iotsitewise.types.parquet.Parquet"]
    """<p>The file is in parquet format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileFormat) -> dict:
    out: dict = {}
    if "csv" in value:
        import aws_sdk_iotsitewise.types.csv

        out["csv"] = aws_sdk_iotsitewise.types.csv.serialize_json(value["csv"])
    if "parquet" in value:
        import aws_sdk_iotsitewise.types.parquet

        out["parquet"] = aws_sdk_iotsitewise.types.parquet.serialize_json(
            value["parquet"]
        )
    return out


def deserialize_json(data: dict) -> FileFormat:
    out: FileFormat = {}  # type: ignore[typeddict-item]
    if "csv" in data:
        import aws_sdk_iotsitewise.types.csv

        out["csv"] = aws_sdk_iotsitewise.types.csv.deserialize_json(data["csv"])
    if "parquet" in data:
        import aws_sdk_iotsitewise.types.parquet

        out["parquet"] = aws_sdk_iotsitewise.types.parquet.deserialize_json(
            data["parquet"]
        )
    return out
