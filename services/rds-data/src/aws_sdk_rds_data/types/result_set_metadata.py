"""Generated from Smithy shape ``com.amazonaws.rdsdata#ResultSetMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.long
    import aws_sdk_rds_data.types.metadata


class ResultSetMetadata(TypedDict, closed=True):
    column_count: "aws_sdk_rds_data.types.long.Long"
    """<p>The number of columns in the result set.</p>"""
    column_metadata: NotRequired["aws_sdk_rds_data.types.metadata.Metadata"]
    """<p>The metadata of the columns in the result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultSetMetadata) -> dict:
    out: dict = {}
    out["columnCount"] = value.get("column_count", 0)
    if "column_metadata" in value:
        import aws_sdk_rds_data.types.metadata

        out["columnMetadata"] = aws_sdk_rds_data.types.metadata.serialize_json(
            value["column_metadata"]
        )
    return out


def deserialize_json(data: dict) -> ResultSetMetadata:
    out: ResultSetMetadata = {}  # type: ignore[typeddict-item]
    if "columnCount" in data:
        out["column_count"] = data["columnCount"]
    else:
        out["column_count"] = 0
    if "columnMetadata" in data:
        import aws_sdk_rds_data.types.metadata

        out["column_metadata"] = aws_sdk_rds_data.types.metadata.deserialize_json(
            data["columnMetadata"]
        )
    return out
