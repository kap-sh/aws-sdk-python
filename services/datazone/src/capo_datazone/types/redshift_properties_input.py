"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftPropertiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.redshift_credentials
    import capo_datazone.types.redshift_lineage_sync_configuration_input
    import capo_datazone.types.redshift_storage_properties


class RedshiftPropertiesInput(TypedDict, closed=True):
    storage: NotRequired[
        "capo_datazone.types.redshift_storage_properties.RedshiftStorageProperties"
    ]
    """<p>The Amazon Redshift storage.</p>"""
    database_name: NotRequired["str"]
    """<p>The Amazon Redshift database name.</p>"""
    host: NotRequired["str"]
    """<p>The Amazon Redshift host.</p>"""
    port: NotRequired["int"]
    """<p>The Amaon Redshift port.</p>"""
    credentials: NotRequired[
        "capo_datazone.types.redshift_credentials.RedshiftCredentials"
    ]
    """<p>The Amaon Redshift credentials.</p>"""
    lineage_sync: NotRequired[
        "capo_datazone.types.redshift_lineage_sync_configuration_input.RedshiftLineageSyncConfigurationInput"
    ]
    """<p>The lineage sync of the Amazon Redshift.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftPropertiesInput) -> dict:
    out: dict = {}
    if "storage" in value:
        import capo_datazone.types.redshift_storage_properties

        out["storage"] = capo_datazone.types.redshift_storage_properties.serialize_json(
            value["storage"]
        )
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "host" in value:
        out["host"] = value["host"]
    if "port" in value:
        out["port"] = value["port"]
    if "credentials" in value:
        import capo_datazone.types.redshift_credentials

        out["credentials"] = capo_datazone.types.redshift_credentials.serialize_json(
            value["credentials"]
        )
    if "lineage_sync" in value:
        import capo_datazone.types.redshift_lineage_sync_configuration_input

        out["lineageSync"] = (
            capo_datazone.types.redshift_lineage_sync_configuration_input.serialize_json(
                value["lineage_sync"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftPropertiesInput:
    out: RedshiftPropertiesInput = {}  # type: ignore[typeddict-item]
    if "storage" in data:
        import capo_datazone.types.redshift_storage_properties

        out["storage"] = (
            capo_datazone.types.redshift_storage_properties.deserialize_json(
                data["storage"]
            )
        )
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "host" in data:
        out["host"] = data["host"]
    if "port" in data:
        out["port"] = data["port"]
    if "credentials" in data:
        import capo_datazone.types.redshift_credentials

        out["credentials"] = capo_datazone.types.redshift_credentials.deserialize_json(
            data["credentials"]
        )
    if "lineageSync" in data:
        import capo_datazone.types.redshift_lineage_sync_configuration_input

        out["lineage_sync"] = (
            capo_datazone.types.redshift_lineage_sync_configuration_input.deserialize_json(
                data["lineageSync"]
            )
        )
    return out
