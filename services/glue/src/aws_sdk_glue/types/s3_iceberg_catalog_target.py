"""Generated from Smithy shape ``com.amazonaws.glue#S3IcebergCatalogTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_options
    import aws_sdk_glue.types.auto_data_quality
    import aws_sdk_glue.types.catalog_schema_change_policy
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class S3IcebergCatalogTarget(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the Iceberg catalog target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The input connection for the Iceberg catalog target.</p>"""
    partition_keys: NotRequired[
        "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>A list of partition keys for the Iceberg table.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table to write to in the catalog.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional connection options for the Iceberg catalog target.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.catalog_schema_change_policy.CatalogSchemaChangePolicy"
    ]
    """<p>The policy for handling schema changes in the catalog target.</p>"""
    auto_data_quality: NotRequired[
        "aws_sdk_glue.types.auto_data_quality.AutoDataQuality"
    ]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 Iceberg catalog target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3IcebergCatalogTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "partition_keys" in value:
        import aws_sdk_glue.types.glue_studio_path_list

        out["PartitionKeys"] = (
            aws_sdk_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    out["Table"] = value["table"]
    out["Database"] = value["database"]
    if "additional_options" in value:
        import aws_sdk_glue.types.additional_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "schema_change_policy" in value:
        import aws_sdk_glue.types.catalog_schema_change_policy

        out["SchemaChangePolicy"] = (
            aws_sdk_glue.types.catalog_schema_change_policy.serialize_aws_json_1_1(
                value["schema_change_policy"]
            )
        )
    if "auto_data_quality" in value:
        import aws_sdk_glue.types.auto_data_quality

        out["AutoDataQuality"] = (
            aws_sdk_glue.types.auto_data_quality.serialize_aws_json_1_1(
                value["auto_data_quality"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3IcebergCatalogTarget:
    out: S3IcebergCatalogTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3IcebergCatalogTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("S3IcebergCatalogTarget.inputs required")
    if "PartitionKeys" in data:
        import aws_sdk_glue.types.glue_studio_path_list

        out["partition_keys"] = (
            aws_sdk_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("S3IcebergCatalogTarget.table required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("S3IcebergCatalogTarget.database required")
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "SchemaChangePolicy" in data:
        import aws_sdk_glue.types.catalog_schema_change_policy

        out["schema_change_policy"] = (
            aws_sdk_glue.types.catalog_schema_change_policy.deserialize_aws_json_1_1(
                data["SchemaChangePolicy"]
            )
        )
    if "AutoDataQuality" in data:
        import aws_sdk_glue.types.auto_data_quality

        out["auto_data_quality"] = (
            aws_sdk_glue.types.auto_data_quality.deserialize_aws_json_1_1(
                data["AutoDataQuality"]
            )
        )
    return out
