"""Generated from Smithy shape ``com.amazonaws.finspace#KxDatabaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.changeset_id
    import capo_finspace.types.database_name
    import capo_finspace.types.kx_database_cache_configurations
    import capo_finspace.types.kx_dataview_configuration
    import capo_finspace.types.kx_dataview_name


class KxDatabaseConfiguration(TypedDict, closed=True):
    database_name: "capo_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database. When this parameter is specified in the structure, S3 with the whole database is included by default.</p>"""
    cache_configurations: NotRequired[
        "capo_finspace.types.kx_database_cache_configurations.KxDatabaseCacheConfigurations"
    ]
    """<p>Configuration details for the disk cache used to increase performance reading from a kdb database mounted to the cluster.</p>"""
    changeset_id: NotRequired["capo_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier of the changeset that is associated with the cluster.</p>"""
    dataview_name: NotRequired["capo_finspace.types.kx_dataview_name.KxDataviewName"]
    """<p> The name of the dataview to be used for caching historical data on disk. </p>"""
    dataview_configuration: NotRequired[
        "capo_finspace.types.kx_dataview_configuration.KxDataviewConfiguration"
    ]
    """<p> The configuration of the dataview to be used with specified cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxDatabaseConfiguration) -> dict:
    out: dict = {}
    out["databaseName"] = value["database_name"]
    if "cache_configurations" in value:
        import capo_finspace.types.kx_database_cache_configurations

        out["cacheConfigurations"] = (
            capo_finspace.types.kx_database_cache_configurations.serialize_json(
                value["cache_configurations"]
            )
        )
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "dataview_name" in value:
        out["dataviewName"] = value["dataview_name"]
    if "dataview_configuration" in value:
        import capo_finspace.types.kx_dataview_configuration

        out["dataviewConfiguration"] = (
            capo_finspace.types.kx_dataview_configuration.serialize_json(
                value["dataview_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KxDatabaseConfiguration:
    out: KxDatabaseConfiguration = {}  # type: ignore[typeddict-item]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("KxDatabaseConfiguration.database_name required")
    if "cacheConfigurations" in data:
        import capo_finspace.types.kx_database_cache_configurations

        out["cache_configurations"] = (
            capo_finspace.types.kx_database_cache_configurations.deserialize_json(
                data["cacheConfigurations"]
            )
        )
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "dataviewName" in data:
        out["dataview_name"] = data["dataviewName"]
    if "dataviewConfiguration" in data:
        import capo_finspace.types.kx_dataview_configuration

        out["dataview_configuration"] = (
            capo_finspace.types.kx_dataview_configuration.deserialize_json(
                data["dataviewConfiguration"]
            )
        )
    return out
