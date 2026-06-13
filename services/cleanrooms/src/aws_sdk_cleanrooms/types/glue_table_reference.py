"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GlueTableReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.commercial_region
    import aws_sdk_cleanrooms.types.glue_database_name
    import aws_sdk_cleanrooms.types.glue_table_name


class GlueTableReference(TypedDict):
    region: NotRequired["aws_sdk_cleanrooms.types.commercial_region.CommercialRegion"]
    """<p>The Amazon Web Services Region where the Glue table is located. This parameter is required to uniquely identify and access tables across different Regions.</p>"""
    table_name: "aws_sdk_cleanrooms.types.glue_table_name.GlueTableName"
    """<p>The name of the Glue table.</p>"""
    database_name: "aws_sdk_cleanrooms.types.glue_database_name.GlueDatabaseName"
    """<p>The name of the database the Glue table belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueTableReference) -> dict:
    out: dict = {}
    if "region" in value:
        import aws_sdk_cleanrooms.types.commercial_region

        out["region"] = aws_sdk_cleanrooms.types.commercial_region.serialize_json(
            value["region"]
        )
    out["tableName"] = value["table_name"]
    out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> GlueTableReference:
    out: GlueTableReference = {}  # type: ignore[typeddict-item]
    if "region" in data:
        import aws_sdk_cleanrooms.types.commercial_region

        out["region"] = aws_sdk_cleanrooms.types.commercial_region.deserialize_json(
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
