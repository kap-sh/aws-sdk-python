"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftPropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.connection_status
    import aws_sdk_datazone.types.redshift_credentials
    import aws_sdk_datazone.types.redshift_lineage_sync_configuration_output
    import aws_sdk_datazone.types.redshift_storage_properties


class RedshiftPropertiesOutput(TypedDict, closed=True):
    storage: NotRequired[
        "aws_sdk_datazone.types.redshift_storage_properties.RedshiftStorageProperties"
    ]
    """<p>The storage in the Amazon Redshift properties.</p>"""
    credentials: NotRequired[
        "aws_sdk_datazone.types.redshift_credentials.RedshiftCredentials"
    ]
    """<p>The Amazon Redshift credentials.</p>"""
    is_provisioned_secret: NotRequired["bool"]
    """<p>Specifies whether Amaon Redshift properties has a provisioned secret.</p>"""
    jdbc_iam_url: NotRequired["str"]
    """<p>The jdbcIam URL of the Amazon Redshift properties.</p>"""
    jdbc_url: NotRequired["str"]
    """<p>The jdbcURL of the Amazon Redshift properties. </p>"""
    redshift_temp_dir: NotRequired["str"]
    """<p>The redshiftTempDir of the Amazon Redshift properties.</p>"""
    lineage_sync: NotRequired[
        "aws_sdk_datazone.types.redshift_lineage_sync_configuration_output.RedshiftLineageSyncConfigurationOutput"
    ]
    """<p>The lineage syn of the Amazon Redshift properties.</p>"""
    status: NotRequired["aws_sdk_datazone.types.connection_status.ConnectionStatus"]
    """<p>The status in the Amazon Redshift properties.</p>"""
    database_name: NotRequired["str"]
    """<p>The Amazon Redshift database name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftPropertiesOutput) -> dict:
    out: dict = {}
    if "storage" in value:
        import aws_sdk_datazone.types.redshift_storage_properties

        out["storage"] = (
            aws_sdk_datazone.types.redshift_storage_properties.serialize_json(
                value["storage"]
            )
        )
    if "credentials" in value:
        import aws_sdk_datazone.types.redshift_credentials

        out["credentials"] = aws_sdk_datazone.types.redshift_credentials.serialize_json(
            value["credentials"]
        )
    if "is_provisioned_secret" in value:
        out["isProvisionedSecret"] = value["is_provisioned_secret"]
    if "jdbc_iam_url" in value:
        out["jdbcIamUrl"] = value["jdbc_iam_url"]
    if "jdbc_url" in value:
        out["jdbcUrl"] = value["jdbc_url"]
    if "redshift_temp_dir" in value:
        out["redshiftTempDir"] = value["redshift_temp_dir"]
    if "lineage_sync" in value:
        import aws_sdk_datazone.types.redshift_lineage_sync_configuration_output

        out["lineageSync"] = (
            aws_sdk_datazone.types.redshift_lineage_sync_configuration_output.serialize_json(
                value["lineage_sync"]
            )
        )
    if "status" in value:
        import aws_sdk_datazone.types.connection_status

        out["status"] = aws_sdk_datazone.types.connection_status.serialize_json(
            value["status"]
        )
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> RedshiftPropertiesOutput:
    out: RedshiftPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "storage" in data:
        import aws_sdk_datazone.types.redshift_storage_properties

        out["storage"] = (
            aws_sdk_datazone.types.redshift_storage_properties.deserialize_json(
                data["storage"]
            )
        )
    if "credentials" in data:
        import aws_sdk_datazone.types.redshift_credentials

        out["credentials"] = (
            aws_sdk_datazone.types.redshift_credentials.deserialize_json(
                data["credentials"]
            )
        )
    if "isProvisionedSecret" in data:
        out["is_provisioned_secret"] = data["isProvisionedSecret"]
    if "jdbcIamUrl" in data:
        out["jdbc_iam_url"] = data["jdbcIamUrl"]
    if "jdbcUrl" in data:
        out["jdbc_url"] = data["jdbcUrl"]
    if "redshiftTempDir" in data:
        out["redshift_temp_dir"] = data["redshiftTempDir"]
    if "lineageSync" in data:
        import aws_sdk_datazone.types.redshift_lineage_sync_configuration_output

        out["lineage_sync"] = (
            aws_sdk_datazone.types.redshift_lineage_sync_configuration_output.deserialize_json(
                data["lineageSync"]
            )
        )
    if "status" in data:
        import aws_sdk_datazone.types.connection_status

        out["status"] = aws_sdk_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    return out
