"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GlueTableReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.commercial_region
    import capo_cleanrooms.types.glue_database_name
    import capo_cleanrooms.types.glue_table_name


class GlueTableReference(TypedDict, closed=True):
    region: NotRequired["capo_cleanrooms.types.commercial_region.CommercialRegion"]
    """<p>The Amazon Web Services Region where the Glue table is located. This parameter is required to uniquely identify and access tables across different Regions.</p>"""
    table_name: "capo_cleanrooms.types.glue_table_name.GlueTableName"
    """<p>The name of the Glue table.</p>"""
    database_name: "capo_cleanrooms.types.glue_database_name.GlueDatabaseName"
    """<p>The name of the database the Glue table belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueTableReference) -> dict:
    out: dict = {}
    if "region" in value:
        import capo_cleanrooms.types.commercial_region

        out["region"] = capo_cleanrooms.types.commercial_region.serialize_json(
            value["region"]
        )
    out["tableName"] = value["table_name"]
    out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> GlueTableReference:
    out: GlueTableReference = {}  # type: ignore[typeddict-item]
    if "region" in data:
        import capo_cleanrooms.types.commercial_region

        out["region"] = capo_cleanrooms.types.commercial_region.deserialize_json(
            data["region"]
        )
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("GlueTableReference.table_name required")
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("GlueTableReference.database_name required")
    return out
