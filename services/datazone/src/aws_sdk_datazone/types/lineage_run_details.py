"""Generated from Smithy shape ``com.amazonaws.datazone#LineageRunDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_sql_query_run_details


class LineageRunDetails(TypedDict):
    sql_query_run_details: NotRequired[
        "aws_sdk_datazone.types.lineage_sql_query_run_details.LineageSqlQueryRunDetails"
    ]
    """<p>The SQL query run details of a data lineage run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageRunDetails) -> dict:
    out: dict = {}
    if "sql_query_run_details" in value:
        import aws_sdk_datazone.types.lineage_sql_query_run_details

        out["sqlQueryRunDetails"] = (
            aws_sdk_datazone.types.lineage_sql_query_run_details.serialize_json(
                value["sql_query_run_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineageRunDetails:
    out: LineageRunDetails = {}  # type: ignore[typeddict-item]
    if "sqlQueryRunDetails" in data:
        import aws_sdk_datazone.types.lineage_sql_query_run_details

        out["sql_query_run_details"] = (
            aws_sdk_datazone.types.lineage_sql_query_run_details.deserialize_json(
                data["sqlQueryRunDetails"]
            )
        )
    return out
