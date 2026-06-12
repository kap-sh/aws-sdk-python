"""Generated from Smithy shape ``com.amazonaws.sagemaker#OfflineStoreConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.data_catalog_config
    import aws_sdk_sagemaker.types.s3_storage_config
    import aws_sdk_sagemaker.types.table_format


class OfflineStoreConfig(TypedDict):
    s3_storage_config: NotRequired[
        "aws_sdk_sagemaker.types.s3_storage_config.S3StorageConfig"
    ]
    """<p>The Amazon Simple Storage (Amazon S3) location of <code>OfflineStore</code>.</p>"""
    disable_glue_table_creation: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Set to <code>True</code> to disable the automatic creation of an Amazon Web Services Glue table when configuring an <code>OfflineStore</code>. If set to <code>True</code> and <code>DataCatalogConfig</code> is provided, Feature Store associates the provided catalog configuration with the feature group without creating a table. In this case, you are responsible for creating and managing the Glue table. If set to <code>True</code> without <code>DataCatalogConfig</code>, no Glue table is created or associated with the feature group. The <code>Iceberg</code> table format is only supported when this is set to <code>False</code>.</p> <p>If set to <code>False</code> and <code>DataCatalogConfig</code> is provided, Feature Store creates the table using the specified names. If set to <code>False</code> without <code>DataCatalogConfig</code>, Feature Store auto-generates the table name following <a href=\"https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html\">Athena's naming recommendations</a>. This applies to both Glue and Apache Iceberg table formats.</p> <p>The default value is <code>False</code>.</p>"""
    data_catalog_config: NotRequired[
        "aws_sdk_sagemaker.types.data_catalog_config.DataCatalogConfig"
    ]
    """<p>The meta data of the Glue table for the <code>OfflineStore</code>. If not provided, Feature Store auto-generates the table name, database, and catalog when the <code>OfflineStore</code> is created. You can optionally provide this configuration to specify custom values. This applies to both Glue and Apache Iceberg table formats.</p>"""
    table_format: NotRequired["aws_sdk_sagemaker.types.table_format.TableFormat"]
    """<p>Format for the offline store table. Supported formats are Glue (Default) and <a href=\"https://iceberg.apache.org/\">Apache Iceberg</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfflineStoreConfig) -> dict:
    out: dict = {}
    if "s3_storage_config" in value:
        import aws_sdk_sagemaker.types.s3_storage_config

        out["S3StorageConfig"] = (
            aws_sdk_sagemaker.types.s3_storage_config.serialize_aws_json_1_1(
                value["s3_storage_config"]
            )
        )
    if "disable_glue_table_creation" in value:
        out["DisableGlueTableCreation"] = value["disable_glue_table_creation"]
    if "data_catalog_config" in value:
        import aws_sdk_sagemaker.types.data_catalog_config

        out["DataCatalogConfig"] = (
            aws_sdk_sagemaker.types.data_catalog_config.serialize_aws_json_1_1(
                value["data_catalog_config"]
            )
        )
    if "table_format" in value:
        import aws_sdk_sagemaker.types.table_format

        out["TableFormat"] = (
            aws_sdk_sagemaker.types.table_format.serialize_aws_json_1_1(
                value["table_format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OfflineStoreConfig:
    out: OfflineStoreConfig = {}  # type: ignore[typeddict-item]
    if "S3StorageConfig" in data:
        import aws_sdk_sagemaker.types.s3_storage_config

        out["s3_storage_config"] = (
            aws_sdk_sagemaker.types.s3_storage_config.deserialize_aws_json_1_1(
                data["S3StorageConfig"]
            )
        )
    if "DisableGlueTableCreation" in data:
        out["disable_glue_table_creation"] = data["DisableGlueTableCreation"]
    if "DataCatalogConfig" in data:
        import aws_sdk_sagemaker.types.data_catalog_config

        out["data_catalog_config"] = (
            aws_sdk_sagemaker.types.data_catalog_config.deserialize_aws_json_1_1(
                data["DataCatalogConfig"]
            )
        )
    if "TableFormat" in data:
        import aws_sdk_sagemaker.types.table_format

        out["table_format"] = (
            aws_sdk_sagemaker.types.table_format.deserialize_aws_json_1_1(
                data["TableFormat"]
            )
        )
    return out
