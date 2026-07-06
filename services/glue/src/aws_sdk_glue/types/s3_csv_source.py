"""Generated from Smithy shape ``com.amazonaws.glue#S3CsvSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean_value
    import aws_sdk_glue.types.boxed_boolean
    import aws_sdk_glue.types.boxed_non_negative_int
    import aws_sdk_glue.types.compression_type
    import aws_sdk_glue.types.enclosed_in_string_properties
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.enclosed_in_string_property_with_quote
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.quote_char
    import aws_sdk_glue.types.s3_direct_source_additional_options
    import aws_sdk_glue.types.separator


class S3CsvSource(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data store.</p>"""
    paths: "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    """<p>A list of the Amazon S3 paths to read from.</p>"""
    compression_type: NotRequired["aws_sdk_glue.types.compression_type.CompressionType"]
    r"""<p>Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are <code>\"gzip\"</code> and <code>\"bzip\"</code>).</p>"""
    exclusions: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    r"""<p>A string containing a JSON list of Unix-style glob patterns to exclude. For example, \"[\\"**.pdf\\"]\" excludes all PDF files. </p>"""
    group_size: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    r"""<p>The target group size in bytes. The default is computed based on the input data size and the size of your cluster. When there are fewer than 50,000 input files, <code>\"groupFiles\"</code> must be set to <code>\"inPartition\"</code> for this to take effect.</p>"""
    group_files: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    r"""<p>Grouping files is turned on by default when the input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter to \"inPartition\". To disable grouping when there are more than 50,000 files, set this parameter to <code>\"none\"</code>.</p>"""
    recurse: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>If set to true, recursively reads files in all subdirectories under the specified paths.</p>"""
    max_band: NotRequired[
        "aws_sdk_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>This option controls the duration in milliseconds after which the s3 listing is likely to be consistent. Files with modification timestamps falling within the last maxBand milliseconds are tracked specially when using JobBookmarks to account for Amazon S3 eventual consistency. Most users don't need to set this option. The default is 900000 milliseconds, or 15 minutes.</p>"""
    max_files_in_band: NotRequired[
        "aws_sdk_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>This option specifies the maximum number of files to save from the last maxBand seconds. If this number is exceeded, extra files are skipped and only processed in the next job run.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.s3_direct_source_additional_options.S3DirectSourceAdditionalOptions"
    ]
    """<p>Specifies additional connection options.</p>"""
    separator: "aws_sdk_glue.types.separator.Separator"
    r"""<p>Specifies the delimiter character. The default is a comma: \",\", but any other character can be specified.</p>"""
    escaper: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property_with_quote.EnclosedInStringPropertyWithQuote"
    ]
    r"""<p>Specifies a character to use for escaping. This option is used only when reading CSV files. The default value is <code>none</code>. If enabled, the character which immediately follows is used as-is, except for a small set of well-known escapes (<code>\n</code>, <code>\r</code>, <code>\t</code>, and <code>\0</code>).</p>"""
    quote_char: "aws_sdk_glue.types.quote_char.QuoteChar"
    r"""<p>Specifies the character to use for quoting. The default is a double quote: <code>'\"'</code>. Set this to <code>-1</code> to turn off quoting entirely.</p>"""
    multiline: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>A Boolean value that specifies whether a single record can span multiple lines. This can occur when a field contains a quoted new-line character. You must set this option to True if any record spans multiple lines. The default value is <code>False</code>, which allows for more aggressive file-splitting during parsing.</p>"""
    with_header: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>A Boolean value that specifies whether to treat the first line as a header. The default value is <code>False</code>.</p>"""
    write_header: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>A Boolean value that specifies whether to write the header to output. The default value is <code>True</code>. </p>"""
    skip_first: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>A Boolean value that specifies whether to skip the first data line. The default value is <code>False</code>.</p>"""
    optimize_performance: "aws_sdk_glue.types.boolean_value.BooleanValue"
    """<p>A Boolean value that specifies whether to use the advanced SIMD CSV reader along with Apache Arrow based columnar memory formats. Only available in Glue version 3.0.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 CSV source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3CsvSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.enclosed_in_string_properties

    out["Paths"] = (
        aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["paths"]
        )
    )
    if "compression_type" in value:
        import aws_sdk_glue.types.compression_type

        out["CompressionType"] = (
            aws_sdk_glue.types.compression_type.serialize_aws_json_1_1(
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
    import aws_sdk_glue.types.separator

    out["Separator"] = aws_sdk_glue.types.separator.serialize_aws_json_1_1(
        value["separator"]
    )
    if "escaper" in value:
        out["Escaper"] = value["escaper"]
    import aws_sdk_glue.types.quote_char

    out["QuoteChar"] = aws_sdk_glue.types.quote_char.serialize_aws_json_1_1(
        value["quote_char"]
    )
    if "multiline" in value:
        out["Multiline"] = value["multiline"]
    if "with_header" in value:
        out["WithHeader"] = value["with_header"]
    if "write_header" in value:
        out["WriteHeader"] = value["write_header"]
    if "skip_first" in value:
        out["SkipFirst"] = value["skip_first"]
    out["OptimizePerformance"] = value.get("optimize_performance", False)
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3CsvSource:
    out: S3CsvSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3CsvSource.name required")
    if "Paths" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["paths"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    else:
        raise DeserializationError("S3CsvSource.paths required")
    if "CompressionType" in data:
        import aws_sdk_glue.types.compression_type

        out["compression_type"] = (
            aws_sdk_glue.types.compression_type.deserialize_aws_json_1_1(
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
    if "Separator" in data:
        import aws_sdk_glue.types.separator

        out["separator"] = aws_sdk_glue.types.separator.deserialize_aws_json_1_1(
            data["Separator"]
        )
    else:
        raise DeserializationError("S3CsvSource.separator required")
    if "Escaper" in data:
        out["escaper"] = data["Escaper"]
    if "QuoteChar" in data:
        import aws_sdk_glue.types.quote_char

        out["quote_char"] = aws_sdk_glue.types.quote_char.deserialize_aws_json_1_1(
            data["QuoteChar"]
        )
    else:
        raise DeserializationError("S3CsvSource.quote_char required")
    if "Multiline" in data:
        out["multiline"] = data["Multiline"]
    if "WithHeader" in data:
        out["with_header"] = data["WithHeader"]
    if "WriteHeader" in data:
        out["write_header"] = data["WriteHeader"]
    if "SkipFirst" in data:
        out["skip_first"] = data["SkipFirst"]
    if "OptimizePerformance" in data:
        out["optimize_performance"] = data["OptimizePerformance"]
    else:
        out["optimize_performance"] = False
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
