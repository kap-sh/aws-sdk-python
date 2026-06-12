"""Generated from Smithy shape ``com.amazonaws.glue#S3HyperDirectTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.auto_data_quality
    import aws_sdk_glue.types.direct_schema_change_policy
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.hyper_target_compression_type
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.target_format


class S3HyperDirectTarget(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The unique identifier for the HyperDirect target node.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>Specifies the input source for the HyperDirect target.</p>"""
    format: NotRequired["aws_sdk_glue.types.target_format.TargetFormat"]
    """<p>Specifies the data output format for the HyperDirect target.</p>"""
    partition_keys: NotRequired[
        "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Defines the partitioning strategy for the output data.</p>"""
    path: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The S3 location where the output data will be written.</p>"""
    compression: NotRequired[
        "aws_sdk_glue.types.hyper_target_compression_type.HyperTargetCompressionType"
    ]
    """<p>The compression type to apply to the output data.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.direct_schema_change_policy.DirectSchemaChangePolicy"
    ]
    """<p>Defines how schema changes are handled during write operations.</p>"""
    auto_data_quality: NotRequired[
        "aws_sdk_glue.types.auto_data_quality.AutoDataQuality"
    ]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 Hyper direct target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 Hyper direct target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3HyperDirectTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "format" in value:
        import aws_sdk_glue.types.target_format

        out["Format"] = aws_sdk_glue.types.target_format.serialize_aws_json_1_1(
            value["format"]
        )
    if "partition_keys" in value:
        import aws_sdk_glue.types.glue_studio_path_list

        out["PartitionKeys"] = (
            aws_sdk_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    out["Path"] = value["path"]
    if "compression" in value:
        import aws_sdk_glue.types.hyper_target_compression_type

        out["Compression"] = (
            aws_sdk_glue.types.hyper_target_compression_type.serialize_aws_json_1_1(
                value["compression"]
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
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3HyperDirectTarget:
    out: S3HyperDirectTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3HyperDirectTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("S3HyperDirectTarget.inputs required")
    if "Format" in data:
        import aws_sdk_glue.types.target_format

        out["format"] = aws_sdk_glue.types.target_format.deserialize_aws_json_1_1(
            data["Format"]
        )
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
        raise DeserializationError("S3HyperDirectTarget.path required")
    if "Compression" in data:
        import aws_sdk_glue.types.hyper_target_compression_type

        out["compression"] = (
            aws_sdk_glue.types.hyper_target_compression_type.deserialize_aws_json_1_1(
                data["Compression"]
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
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
