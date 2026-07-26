"""Generated from Smithy shape ``com.amazonaws.glue#OracleSQLCatalogSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name


class OracleSQLCatalogSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data source.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OracleSQLCatalogSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OracleSQLCatalogSource:
    out: OracleSQLCatalogSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("OracleSQLCatalogSource.name required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("OracleSQLCatalogSource.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("OracleSQLCatalogSource.table required")
    return out
