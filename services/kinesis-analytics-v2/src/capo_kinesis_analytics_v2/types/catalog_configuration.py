"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CatalogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.glue_data_catalog_configuration


class CatalogConfiguration(TypedDict, closed=True):
    glue_data_catalog_configuration: "capo_kinesis_analytics_v2.types.glue_data_catalog_configuration.GlueDataCatalogConfiguration"
    """<p>The configuration parameters for the default Amazon Glue database. You use this database for Apache Flink SQL queries and table API transforms that you write in a Managed Service for Apache Flink Studio notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.glue_data_catalog_configuration

    out["GlueDataCatalogConfiguration"] = (
        capo_kinesis_analytics_v2.types.glue_data_catalog_configuration.serialize_aws_json_1_1(
            value["glue_data_catalog_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogConfiguration:
    out: CatalogConfiguration = {}  # type: ignore[typeddict-item]
    if "GlueDataCatalogConfiguration" in data:
        import capo_kinesis_analytics_v2.types.glue_data_catalog_configuration

        out["glue_data_catalog_configuration"] = (
            capo_kinesis_analytics_v2.types.glue_data_catalog_configuration.deserialize_aws_json_1_1(
                data["GlueDataCatalogConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CatalogConfiguration.glue_data_catalog_configuration required"
        )
    return out
