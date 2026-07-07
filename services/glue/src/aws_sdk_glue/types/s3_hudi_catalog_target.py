"""Generated from Smithy shape ``com.amazonaws.glue#S3HudiCatalogTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_options
    import aws_sdk_glue.types.auto_data_quality
    import aws_sdk_glue.types.catalog_schema_change_policy
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class S3HudiCatalogTarget(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    partition_keys: NotRequired[
        "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies native partitioning using a sequence of keys.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to write to.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    additional_options: "aws_sdk_glue.types.additional_options.AdditionalOptions"
    """<p>Specifies additional connection options for the connector.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.catalog_schema_change_policy.CatalogSchemaChangePolicy"
    ]
    """<p>A policy that specifies update behavior for the crawler.</p>"""
    auto_data_quality: NotRequired[
        "aws_sdk_glue.types.auto_data_quality.AutoDataQuality"
    ]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 Hudi catalog target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 Hudi catalog target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3HudiCatalogTarget) -> dict:
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
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3HudiCatalogTarget:
    out: S3HudiCatalogTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3HudiCatalogTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("S3HudiCatalogTarget.inputs required")
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
        raise DeserializationError("S3HudiCatalogTarget.table required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("S3HudiCatalogTarget.database required")
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    else:
        raise DeserializationError("S3HudiCatalogTarget.additional_options required")
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
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
