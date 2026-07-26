"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AthenaTableReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.athena_catalog_name
    import capo_cleanrooms.types.athena_database_name
    import capo_cleanrooms.types.athena_output_location
    import capo_cleanrooms.types.athena_table_name
    import capo_cleanrooms.types.athena_work_group
    import capo_cleanrooms.types.commercial_region


class AthenaTableReference(TypedDict, closed=True):
    region: NotRequired["capo_cleanrooms.types.commercial_region.CommercialRegion"]
    """<p>The Amazon Web Services Region where the Athena table is located. This parameter is required to uniquely identify and access tables across different Regions.</p>"""
    work_group: "capo_cleanrooms.types.athena_work_group.AthenaWorkGroup"
    """<p> The workgroup of the Athena table reference.</p>"""
    output_location: NotRequired[
        "capo_cleanrooms.types.athena_output_location.AthenaOutputLocation"
    ]
    """<p> The output location for the Athena table.</p>"""
    database_name: "capo_cleanrooms.types.athena_database_name.AthenaDatabaseName"
    """<p> The database name.</p>"""
    table_name: "capo_cleanrooms.types.athena_table_name.AthenaTableName"
    """<p> The table reference.</p>"""
    catalog_name: NotRequired[
        "capo_cleanrooms.types.athena_catalog_name.AthenaCatalogName"
    ]
    """<p> The catalog name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AthenaTableReference) -> dict:
    out: dict = {}
    if "region" in value:
        import capo_cleanrooms.types.commercial_region

        out["region"] = capo_cleanrooms.types.commercial_region.serialize_json(
            value["region"]
        )
    out["workGroup"] = value["work_group"]
    if "output_location" in value:
        out["outputLocation"] = value["output_location"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    if "catalog_name" in value:
        out["catalogName"] = value["catalog_name"]
    return out


def deserialize_json(data: dict) -> AthenaTableReference:
    out: AthenaTableReference = {}  # type: ignore[typeddict-item]
    if "region" in data:
        import capo_cleanrooms.types.commercial_region

        out["region"] = capo_cleanrooms.types.commercial_region.deserialize_json(
            data["region"]
        )
    if "workGroup" in data:
        out["work_group"] = data["workGroup"]
    else:
        raise DeserializationError("AthenaTableReference.work_group required")
    if "outputLocation" in data:
        out["output_location"] = data["outputLocation"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("AthenaTableReference.database_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("AthenaTableReference.table_name required")
    if "catalogName" in data:
        out["catalog_name"] = data["catalogName"]
    return out
