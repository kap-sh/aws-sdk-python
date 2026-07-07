"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CatalogConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.glue_data_catalog_configuration_description


class CatalogConfigurationDescription(TypedDict, closed=True):
    glue_data_catalog_configuration_description: "aws_sdk_kinesis_analytics_v2.types.glue_data_catalog_configuration_description.GlueDataCatalogConfigurationDescription"
    """<p>The configuration parameters for the default Amazon Glue database. You use this database for SQL queries that you write in a Managed Service for Apache Flink Studio notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogConfigurationDescription) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.glue_data_catalog_configuration_description

    out["GlueDataCatalogConfigurationDescription"] = (
        aws_sdk_kinesis_analytics_v2.types.glue_data_catalog_configuration_description.serialize_aws_json_1_1(
            value["glue_data_catalog_configuration_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogConfigurationDescription:
    out: CatalogConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "GlueDataCatalogConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.glue_data_catalog_configuration_description

        out["glue_data_catalog_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.glue_data_catalog_configuration_description.deserialize_aws_json_1_1(
                data["GlueDataCatalogConfigurationDescription"]
            )
        )
    else:
        raise DeserializationError(
            "CatalogConfigurationDescription.glue_data_catalog_configuration_description required"
        )
    return out
