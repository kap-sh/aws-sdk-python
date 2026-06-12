"""Generated from Smithy shape ``com.amazonaws.glue#S3HudiDirectTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_options
    import aws_sdk_glue.types.auto_data_quality
    import aws_sdk_glue.types.direct_schema_change_policy
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.hudi_target_compression_type
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.number_target_partitions_string
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.target_format


class S3HudiDirectTarget(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    path: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The Amazon S3 path of your Hudi data source to write to.</p>"""
    compression: (
        "aws_sdk_glue.types.hudi_target_compression_type.HudiTargetCompressionType"
    )
    """<p>Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are <code>\"gzip\"</code> and <code>\"bzip\"</code>).</p>"""
    number_target_partitions: NotRequired[
        "aws_sdk_glue.types.number_target_partitions_string.NumberTargetPartitionsString"
    ]
    """<p>Specifies the number of target partitions for distributing Hudi dataset files across Amazon S3.</p>"""
    partition_keys: NotRequired[
        "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies native partitioning using a sequence of keys.</p>"""
    format: "aws_sdk_glue.types.target_format.TargetFormat"
    """<p>Specifies the data output format for the target.</p>"""
    additional_options: "aws_sdk_glue.types.additional_options.AdditionalOptions"
    """<p>Specifies additional connection options for the connector.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.direct_schema_change_policy.DirectSchemaChangePolicy"
    ]
    """<p>A policy that specifies update behavior for the crawler.</p>"""
    auto_data_quality: NotRequired[
        "aws_sdk_glue.types.auto_data_quality.AutoDataQuality"
    ]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 Hudi direct target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3HudiDirectTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Path"] = value["path"]
    import aws_sdk_glue.types.hudi_target_compression_type

    out["Compression"] = (
        aws_sdk_glue.types.hudi_target_compression_type.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    if "number_target_partitions" in value:
        out["NumberTargetPartitions"] = value["number_target_partitions"]
    if "partition_keys" in value:
        import aws_sdk_glue.types.glue_studio_path_list

        out["PartitionKeys"] = (
            aws_sdk_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    import aws_sdk_glue.types.target_format

    out["Format"] = aws_sdk_glue.types.target_format.serialize_aws_json_1_1(
        value["format"]
    )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> S3HudiDirectTarget:
    out: S3HudiDirectTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3HudiDirectTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("S3HudiDirectTarget.inputs required")
    if "Path" in data:
        out["path"] = data["Path"]
    else:
        raise DeserializationError("S3HudiDirectTarget.path required")
    if "Compression" in data:
        import aws_sdk_glue.types.hudi_target_compression_type

        out["compression"] = (
            aws_sdk_glue.types.hudi_target_compression_type.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        raise DeserializationError("S3HudiDirectTarget.compression required")
    if "NumberTargetPartitions" in data:
        out["number_target_partitions"] = data["NumberTargetPartitions"]
    if "PartitionKeys" in data:
        import aws_sdk_glue.types.glue_studio_path_list

        out["partition_keys"] = (
            aws_sdk_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if "Format" in data:
        import aws_sdk_glue.types.target_format

        out["format"] = aws_sdk_glue.types.target_format.deserialize_aws_json_1_1(
            data["Format"]
        )
    else:
        raise DeserializationError("S3HudiDirectTarget.format required")
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    else:
        raise DeserializationError("S3HudiDirectTarget.additional_options required")
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
    return out
