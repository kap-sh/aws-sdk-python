"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecutionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.catalog_name_string
    import capo_athena.types.database_string


class QueryExecutionContext(TypedDict, closed=True):
    database: NotRequired["capo_athena.types.database_string.DatabaseString"]
    """<p>The name of the database used in the query execution. The database must exist in the catalog.</p>"""
    catalog: NotRequired["capo_athena.types.catalog_name_string.CatalogNameString"]
    """<p>The name of the data catalog used in the query execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryExecutionContext) -> dict:
    out: dict = {}
    if "database" in value:
        out["Database"] = value["database"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryExecutionContext:
    out: QueryExecutionContext = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        out["database"] = data["Database"]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    return out
