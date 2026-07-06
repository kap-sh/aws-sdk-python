"""Generated from Smithy shape ``com.amazonaws.glue#S3ExcelSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_boolean
    import aws_sdk_glue.types.boxed_long
    import aws_sdk_glue.types.boxed_non_negative_int
    import aws_sdk_glue.types.enclosed_in_string_properties
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.parquet_compression_type
    import aws_sdk_glue.types.s3_direct_source_additional_options


class S3ExcelSource(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the S3 Excel data source.</p>"""
    paths: "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    """<p>The S3 paths where the Excel files are located.</p>"""
    compression_type: NotRequired[
        "aws_sdk_glue.types.parquet_compression_type.ParquetCompressionType"
    ]
    """<p>The compression format used for the Excel files.</p>"""
    exclusions: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    """<p>Patterns to exclude specific files or paths from processing.</p>"""
    group_size: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Defines the size of file groups for batch processing.</p>"""
    group_files: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies how files should be grouped for processing.</p>"""
    recurse: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether to recursively process subdirectories.</p>"""
    max_band: NotRequired[
        "aws_sdk_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The maximum number of processing bands to use.</p>"""
    max_files_in_band: NotRequired[
        "aws_sdk_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The maximum number of files to process in each band.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.s3_direct_source_additional_options.S3DirectSourceAdditionalOptions"
    ]
    """<p>Additional configuration options for S3 direct source processing.</p>"""
    number_rows: NotRequired["aws_sdk_glue.types.boxed_long.BoxedLong"]
    """<p>The number of rows to process from each Excel file.</p>"""
    skip_footer: NotRequired[
        "aws_sdk_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The number of rows to skip at the end of each Excel file.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>The Glue schemas to apply to the processed data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ExcelSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.enclosed_in_string_properties

    out["Paths"] = (
        aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["paths"]
        )
    )
    if "compression_type" in value:
        import aws_sdk_glue.types.parquet_compression_type

        out["CompressionType"] = (
            aws_sdk_glue.types.parquet_compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "exclusions" in value:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["Exclusions"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
                value["exclusions"]
            )
        )
    if "group_size" in value:
        out["GroupSize"] = value["group_size"]
    if "group_files" in value:
        out["GroupFiles"] = value["group_files"]
    if "recurse" in value:
        out["Recurse"] = value["recurse"]
    if "max_band" in value:
        out["MaxBand"] = value["max_band"]
    if "max_files_in_band" in value:
        out["MaxFilesInBand"] = value["max_files_in_band"]
    if "additional_options" in value:
        import aws_sdk_glue.types.s3_direct_source_additional_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.s3_direct_source_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "number_rows" in value:
        out["NumberRows"] = value["number_rows"]
    if "skip_footer" in value:
        out["SkipFooter"] = value["skip_footer"]
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ExcelSource:
    out: S3ExcelSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3ExcelSource.name required")
    if "Paths" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["paths"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    else:
        raise DeserializationError("S3ExcelSource.paths required")
    if "CompressionType" in data:
        import aws_sdk_glue.types.parquet_compression_type

        out["compression_type"] = (
            aws_sdk_glue.types.parquet_compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if "Exclusions" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["exclusions"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Exclusions"]
            )
        )
    if "GroupSize" in data:
        out["group_size"] = data["GroupSize"]
    if "GroupFiles" in data:
        out["group_files"] = data["GroupFiles"]
    if "Recurse" in data:
        out["recurse"] = data["Recurse"]
    if "MaxBand" in data:
        out["max_band"] = data["MaxBand"]
    if "MaxFilesInBand" in data:
        out["max_files_in_band"] = data["MaxFilesInBand"]
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.s3_direct_source_additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.s3_direct_source_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "NumberRows" in data:
        out["number_rows"] = data["NumberRows"]
    if "SkipFooter" in data:
        out["skip_footer"] = data["SkipFooter"]
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
