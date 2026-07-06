"""Generated from Smithy shape ``com.amazonaws.firehose#ParquetSerDe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.block_size_bytes
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.non_negative_integer_object
    import aws_sdk_firehose.types.parquet_compression
    import aws_sdk_firehose.types.parquet_page_size_bytes
    import aws_sdk_firehose.types.parquet_writer_version


class ParquetSerDe(TypedDict, closed=True):
    block_size_bytes: NotRequired[
        "aws_sdk_firehose.types.block_size_bytes.BlockSizeBytes"
    ]
    """<p>The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.</p>"""
    page_size_bytes: NotRequired[
        "aws_sdk_firehose.types.parquet_page_size_bytes.ParquetPageSizeBytes"
    ]
    """<p>The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.</p>"""
    compression: NotRequired[
        "aws_sdk_firehose.types.parquet_compression.ParquetCompression"
    ]
    """<p>The compression code to use over data blocks. The possible values are <code>UNCOMPRESSED</code>, <code>SNAPPY</code>, and <code>GZIP</code>, with the default being <code>SNAPPY</code>. Use <code>SNAPPY</code> for higher decompression speed. Use <code>GZIP</code> if the compression ratio is more important than speed.</p>"""
    enable_dictionary_compression: NotRequired[
        "aws_sdk_firehose.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether to enable dictionary compression.</p>"""
    max_padding_bytes: NotRequired[
        "aws_sdk_firehose.types.non_negative_integer_object.NonNegativeIntegerObject"
    ]
    """<p>The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.</p>"""
    writer_version: NotRequired[
        "aws_sdk_firehose.types.parquet_writer_version.ParquetWriterVersion"
    ]
    """<p>Indicates the version of row format to output. The possible values are <code>V1</code> and <code>V2</code>. The default is <code>V1</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParquetSerDe) -> dict:
    out: dict = {}
    if "block_size_bytes" in value:
        out["BlockSizeBytes"] = value["block_size_bytes"]
    if "page_size_bytes" in value:
        out["PageSizeBytes"] = value["page_size_bytes"]
    if "compression" in value:
        import aws_sdk_firehose.types.parquet_compression

        out["Compression"] = (
            aws_sdk_firehose.types.parquet_compression.serialize_aws_json_1_1(
                value["compression"]
            )
        )
    if "enable_dictionary_compression" in value:
        out["EnableDictionaryCompression"] = value["enable_dictionary_compression"]
    if "max_padding_bytes" in value:
        out["MaxPaddingBytes"] = value["max_padding_bytes"]
    if "writer_version" in value:
        import aws_sdk_firehose.types.parquet_writer_version

        out["WriterVersion"] = (
            aws_sdk_firehose.types.parquet_writer_version.serialize_aws_json_1_1(
                value["writer_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParquetSerDe:
    out: ParquetSerDe = {}  # type: ignore[typeddict-item]
    if "BlockSizeBytes" in data:
        out["block_size_bytes"] = data["BlockSizeBytes"]
    if "PageSizeBytes" in data:
        out["page_size_bytes"] = data["PageSizeBytes"]
    if "Compression" in data:
        import aws_sdk_firehose.types.parquet_compression

        out["compression"] = (
            aws_sdk_firehose.types.parquet_compression.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    if "EnableDictionaryCompression" in data:
        out["enable_dictionary_compression"] = data["EnableDictionaryCompression"]
    if "MaxPaddingBytes" in data:
        out["max_padding_bytes"] = data["MaxPaddingBytes"]
    if "WriterVersion" in data:
        import aws_sdk_firehose.types.parquet_writer_version

        out["writer_version"] = (
            aws_sdk_firehose.types.parquet_writer_version.deserialize_aws_json_1_1(
                data["WriterVersion"]
            )
        )
    return out
