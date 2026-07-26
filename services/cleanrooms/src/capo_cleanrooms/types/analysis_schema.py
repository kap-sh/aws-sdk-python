"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.query_tables


class AnalysisSchema(TypedDict, closed=True):
    referenced_tables: NotRequired["capo_cleanrooms.types.query_tables.QueryTables"]
    """<p>The tables referenced in the analysis schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSchema) -> dict:
    out: dict = {}
    if "referenced_tables" in value:
        import capo_cleanrooms.types.query_tables

        out["referencedTables"] = capo_cleanrooms.types.query_tables.serialize_json(
            value["referenced_tables"]
        )
    return out


def deserialize_json(data: dict) -> AnalysisSchema:
    out: AnalysisSchema = {}  # type: ignore[typeddict-item]
    if "referencedTables" in data:
        import capo_cleanrooms.types.query_tables

        out["referenced_tables"] = capo_cleanrooms.types.query_tables.deserialize_json(
            data["referencedTables"]
        )
    return out
