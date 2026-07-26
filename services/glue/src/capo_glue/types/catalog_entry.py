"""Generated from Smithy shape ``com.amazonaws.glue#CatalogEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.name_string


class CatalogEntry(TypedDict, closed=True):
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The database in which the table metadata resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table in question.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogEntry) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogEntry:
    out: CatalogEntry = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("CatalogEntry.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("CatalogEntry.table_name required")
    return out
