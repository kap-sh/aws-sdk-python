"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CatalogConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.glue_data_catalog_configuration_update


class CatalogConfigurationUpdate(TypedDict, closed=True):
    glue_data_catalog_configuration_update: "capo_kinesis_analytics_v2.types.glue_data_catalog_configuration_update.GlueDataCatalogConfigurationUpdate"
    """<p>Updates to the configuration parameters for the default Amazon Glue database. You use this database for SQL queries that you write in a Managed Service for Apache Flink Studio notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogConfigurationUpdate) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.glue_data_catalog_configuration_update

    out["GlueDataCatalogConfigurationUpdate"] = (
        capo_kinesis_analytics_v2.types.glue_data_catalog_configuration_update.serialize_aws_json_1_1(
            value["glue_data_catalog_configuration_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogConfigurationUpdate:
    out: CatalogConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "GlueDataCatalogConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.glue_data_catalog_configuration_update

        out["glue_data_catalog_configuration_update"] = (
            capo_kinesis_analytics_v2.types.glue_data_catalog_configuration_update.deserialize_aws_json_1_1(
                data["GlueDataCatalogConfigurationUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "CatalogConfigurationUpdate.glue_data_catalog_configuration_update required"
        )
    return out
