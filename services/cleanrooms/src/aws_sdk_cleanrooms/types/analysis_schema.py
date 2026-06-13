"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.query_tables


class AnalysisSchema(TypedDict):
    referenced_tables: NotRequired["aws_sdk_cleanrooms.types.query_tables.QueryTables"]
    """<p>The tables referenced in the analysis schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSchema) -> dict:
    out: dict = {}
    if "referenced_tables" in value:
        import aws_sdk_cleanrooms.types.query_tables

        out["referencedTables"] = aws_sdk_cleanrooms.types.query_tables.serialize_json(
            value["referenced_tables"]
        )
    return out


def deserialize_json(data: dict) -> AnalysisSchema:
    out: AnalysisSchema = {}  # type: ignore[typeddict-item]
    if "referencedTables" in data:
        import aws_sdk_cleanrooms.types.query_tables

        out["referenced_tables"] = (
            aws_sdk_cleanrooms.types.query_tables.deserialize_json(
                data["referencedTables"]
            )
        )
    return out
