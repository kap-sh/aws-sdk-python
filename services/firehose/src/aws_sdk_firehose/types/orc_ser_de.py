"""Generated from Smithy shape ``com.amazonaws.firehose#OrcSerDe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.block_size_bytes
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.list_of_non_empty_strings_without_whitespace
    import aws_sdk_firehose.types.orc_compression
    import aws_sdk_firehose.types.orc_format_version
    import aws_sdk_firehose.types.orc_row_index_stride
    import aws_sdk_firehose.types.orc_stripe_size_bytes
    import aws_sdk_firehose.types.proportion


class OrcSerDe(TypedDict, closed=True):
    stripe_size_bytes: NotRequired[
        "aws_sdk_firehose.types.orc_stripe_size_bytes.OrcStripeSizeBytes"
    ]
    """<p>The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.</p>"""
    block_size_bytes: NotRequired[
        "aws_sdk_firehose.types.block_size_bytes.BlockSizeBytes"
    ]
    """<p>The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.</p>"""
    row_index_stride: NotRequired[
        "aws_sdk_firehose.types.orc_row_index_stride.OrcRowIndexStride"
    ]
    """<p>The number of rows between index entries. The default is 10,000 and the minimum is 1,000.</p>"""
    enable_padding: NotRequired["aws_sdk_firehose.types.boolean_object.BooleanObject"]
    """<p>Set this to <code>true</code> to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is <code>false</code>.</p>"""
    padding_tolerance: NotRequired["aws_sdk_firehose.types.proportion.Proportion"]
    """<p>A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.</p> <p>For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.</p> <p>Firehose ignores this parameter when <a>OrcSerDe$EnablePadding</a> is <code>false</code>.</p>"""
    compression: NotRequired["aws_sdk_firehose.types.orc_compression.OrcCompression"]
    """<p>The compression code to use over data blocks. The default is <code>SNAPPY</code>.</p>"""
    bloom_filter_columns: NotRequired[
        "aws_sdk_firehose.types.list_of_non_empty_strings_without_whitespace.ListOfNonEmptyStringsWithoutWhitespace"
    ]
    """<p>The column names for which you want Firehose to create bloom filters. The default is <code>null</code>.</p>"""
    bloom_filter_false_positive_probability: NotRequired[
        "aws_sdk_firehose.types.proportion.Proportion"
    ]
    """<p>The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.</p>"""
    dictionary_key_threshold: NotRequired[
        "aws_sdk_firehose.types.proportion.Proportion"
    ]
    """<p>Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.</p>"""
    format_version: NotRequired[
        "aws_sdk_firehose.types.orc_format_version.OrcFormatVersion"
    ]
    """<p>The version of the file to write. The possible values are <code>V0_11</code> and <code>V0_12</code>. The default is <code>V0_12</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrcSerDe) -> dict:
    out: dict = {}
    if "stripe_size_bytes" in value:
        out["StripeSizeBytes"] = value["stripe_size_bytes"]
    if "block_size_bytes" in value:
        out["BlockSizeBytes"] = value["block_size_bytes"]
    if "row_index_stride" in value:
        out["RowIndexStride"] = value["row_index_stride"]
    if "enable_padding" in value:
        out["EnablePadding"] = value["enable_padding"]
    if "padding_tolerance" in value:
        out["PaddingTolerance"] = value["padding_tolerance"]
    if "compression" in value:
        import aws_sdk_firehose.types.orc_compression

        out["Compression"] = (
            aws_sdk_firehose.types.orc_compression.serialize_aws_json_1_1(
                value["compression"]
            )
        )
    if "bloom_filter_columns" in value:
        import aws_sdk_firehose.types.list_of_non_empty_strings_without_whitespace

        out["BloomFilterColumns"] = (
            aws_sdk_firehose.types.list_of_non_empty_strings_without_whitespace.serialize_aws_json_1_1(
                value["bloom_filter_columns"]
            )
        )
    if "bloom_filter_false_positive_probability" in value:
        out["BloomFilterFalsePositiveProbability"] = value[
            "bloom_filter_false_positive_probability"
        ]
    if "dictionary_key_threshold" in value:
        out["DictionaryKeyThreshold"] = value["dictionary_key_threshold"]
    if "format_version" in value:
        import aws_sdk_firehose.types.orc_format_version

        out["FormatVersion"] = (
            aws_sdk_firehose.types.orc_format_version.serialize_aws_json_1_1(
                value["format_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrcSerDe:
    out: OrcSerDe = {}  # type: ignore[typeddict-item]
    if "StripeSizeBytes" in data:
        out["stripe_size_bytes"] = data["StripeSizeBytes"]
    if "BlockSizeBytes" in data:
        out["block_size_bytes"] = data["BlockSizeBytes"]
    if "RowIndexStride" in data:
        out["row_index_stride"] = data["RowIndexStride"]
    if "EnablePadding" in data:
        out["enable_padding"] = data["EnablePadding"]
    if "PaddingTolerance" in data:
        out["padding_tolerance"] = data["PaddingTolerance"]
    if "Compression" in data:
        import aws_sdk_firehose.types.orc_compression

        out["compression"] = (
            aws_sdk_firehose.types.orc_compression.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    if "BloomFilterColumns" in data:
        import aws_sdk_firehose.types.list_of_non_empty_strings_without_whitespace

        out["bloom_filter_columns"] = (
            aws_sdk_firehose.types.list_of_non_empty_strings_without_whitespace.deserialize_aws_json_1_1(
                data["BloomFilterColumns"]
            )
        )
    if "BloomFilterFalsePositiveProbability" in data:
        out["bloom_filter_false_positive_probability"] = data[
            "BloomFilterFalsePositiveProbability"
        ]
    if "DictionaryKeyThreshold" in data:
        out["dictionary_key_threshold"] = data["DictionaryKeyThreshold"]
    if "FormatVersion" in data:
        import aws_sdk_firehose.types.orc_format_version

        out["format_version"] = (
            aws_sdk_firehose.types.orc_format_version.deserialize_aws_json_1_1(
                data["FormatVersion"]
            )
        )
    return out
