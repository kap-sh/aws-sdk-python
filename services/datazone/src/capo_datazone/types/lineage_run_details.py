"""Generated from Smithy shape ``com.amazonaws.datazone#LineageRunDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.lineage_sql_query_run_details


class LineageRunDetails(TypedDict, closed=True):
    sql_query_run_details: NotRequired[
        "capo_datazone.types.lineage_sql_query_run_details.LineageSqlQueryRunDetails"
    ]
    """<p>The SQL query run details of a data lineage run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageRunDetails) -> dict:
    out: dict = {}
    if "sql_query_run_details" in value:
        import capo_datazone.types.lineage_sql_query_run_details

        out["sqlQueryRunDetails"] = (
            capo_datazone.types.lineage_sql_query_run_details.serialize_json(
                value["sql_query_run_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineageRunDetails:
    out: LineageRunDetails = {}  # type: ignore[typeddict-item]
    if "sqlQueryRunDetails" in data:
        import capo_datazone.types.lineage_sql_query_run_details

        out["sql_query_run_details"] = (
            capo_datazone.types.lineage_sql_query_run_details.deserialize_json(
                data["sqlQueryRunDetails"]
            )
        )
    return out
