"""Generated from Smithy shape ``com.amazonaws.glue#S3IcebergDirectTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_options
    import aws_sdk_glue.types.auto_data_quality
    import aws_sdk_glue.types.direct_schema_change_policy
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.iceberg_target_compression_type
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.number_target_partitions_string
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.target_format


class S3IcebergDirectTarget(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>Specifies the unique identifier for the Iceberg target node in your data pipeline.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>Defines the single input source that provides data to this Iceberg target.</p>"""
    partition_keys: NotRequired[
        "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies the columns used to partition the Iceberg table data in S3.</p>"""
    path: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>Defines the S3 location where the Iceberg table data will be stored.</p>"""
    format: "aws_sdk_glue.types.target_format.TargetFormat"
    """<p>Specifies the file format used for storing Iceberg table data (e.g., Parquet, ORC).</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Provides additional configuration options for customizing the Iceberg table behavior.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.direct_schema_change_policy.DirectSchemaChangePolicy"
    ]
    """<p>Defines how schema changes are handled when writing data to the Iceberg table.</p>"""
    auto_data_quality: NotRequired[
        "aws_sdk_glue.types.auto_data_quality.AutoDataQuality"
    ]
    compression: "aws_sdk_glue.types.iceberg_target_compression_type.IcebergTargetCompressionType"
    """<p>Specifies the compression codec used for Iceberg table files in S3.</p>"""
    number_target_partitions: NotRequired[
        "aws_sdk_glue.types.number_target_partitions_string.NumberTargetPartitionsString"
    ]
    """<p>Sets the number of target partitions for distributing Iceberg table files across S3.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 Iceberg direct target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3IcebergDirectTarget) -> dict:
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
    out["Path"] = value["path"]
    import aws_sdk_glue.types.target_format

    out["Format"] = aws_sdk_glue.types.target_format.serialize_aws_json_1_1(
        value["format"]
    )
    if "additional_options" in value:
        import aws_sdk_glue.types.additional_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "schema_change_policy" in value:
        import aws_sdk_glue.types.direct_schema_change_policy

        out["SchemaChangePolicy"] = (
            aws_sdk_glue.types.direct_schema_change_policy.serialize_aws_json_1_1(
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
    import aws_sdk_glue.types.iceberg_target_compression_type

    out["Compression"] = (
        aws_sdk_glue.types.iceberg_target_compression_type.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    if "number_target_partitions" in value:
        out["NumberTargetPartitions"] = value["number_target_partitions"]
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3IcebergDirectTarget:
    out: S3IcebergDirectTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3IcebergDirectTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("S3IcebergDirectTarget.inputs required")
    if "PartitionKeys" in data:
        import aws_sdk_glue.types.glue_studio_path_list

        out["partition_keys"] = (
            aws_sdk_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if "Path" in data:
        out["path"] = data["Path"]
    else:
        raise DeserializationError("S3IcebergDirectTarget.path required")
    if "Format" in data:
        import aws_sdk_glue.types.target_format

        out["format"] = aws_sdk_glue.types.target_format.deserialize_aws_json_1_1(
            data["Format"]
        )
    else:
        raise DeserializationError("S3IcebergDirectTarget.format required")
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "SchemaChangePolicy" in data:
        import aws_sdk_glue.types.direct_schema_change_policy

        out["schema_change_policy"] = (
            aws_sdk_glue.types.direct_schema_change_policy.deserialize_aws_json_1_1(
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
    if "Compression" in data:
        import aws_sdk_glue.types.iceberg_target_compression_type

        out["compression"] = (
            aws_sdk_glue.types.iceberg_target_compression_type.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        raise DeserializationError("S3IcebergDirectTarget.compression required")
    if "NumberTargetPartitions" in data:
        out["number_target_partitions"] = data["NumberTargetPartitions"]
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
