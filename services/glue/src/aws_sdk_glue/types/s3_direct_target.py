"""Generated from Smithy shape ``com.amazonaws.glue#S3DirectTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.auto_data_quality
    import aws_sdk_glue.types.direct_schema_change_policy
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.number_target_partitions_string
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.target_format


class S3DirectTarget(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    partition_keys: NotRequired[
        "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies native partitioning using a sequence of keys.</p>"""
    path: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>A single Amazon S3 path to write to.</p>"""
    compression: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    r"""<p>Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are <code>\"gzip\"</code> and <code>\"bzip\"</code>).</p>"""
    number_target_partitions: NotRequired[
        "aws_sdk_glue.types.number_target_partitions_string.NumberTargetPartitionsString"
    ]
    """<p>Specifies the number of target partitions when writing data directly to Amazon S3.</p>"""
    format: "aws_sdk_glue.types.target_format.TargetFormat"
    """<p>Specifies the data output format for the target.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.direct_schema_change_policy.DirectSchemaChangePolicy"
    ]
    """<p>A policy that specifies update behavior for the crawler.</p>"""
    auto_data_quality: NotRequired[
        "aws_sdk_glue.types.auto_data_quality.AutoDataQuality"
    ]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 direct target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 direct target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DirectTarget) -> dict:
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
    if "compression" in value:
        out["Compression"] = value["compression"]
    if "number_target_partitions" in value:
        out["NumberTargetPartitions"] = value["number_target_partitions"]
    import aws_sdk_glue.types.target_format

    out["Format"] = aws_sdk_glue.types.target_format.serialize_aws_json_1_1(
        value["format"]
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


def deserialize_aws_json_1_1(data: dict) -> S3DirectTarget:
    out: S3DirectTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3DirectTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("S3DirectTarget.inputs required")
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
        raise DeserializationError("S3DirectTarget.path required")
    if "Compression" in data:
        out["compression"] = data["Compression"]
    if "NumberTargetPartitions" in data:
        out["number_target_partitions"] = data["NumberTargetPartitions"]
    if "Format" in data:
        import aws_sdk_glue.types.target_format

        out["format"] = aws_sdk_glue.types.target_format.deserialize_aws_json_1_1(
            data["Format"]
        )
    else:
        raise DeserializationError("S3DirectTarget.format required")
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
