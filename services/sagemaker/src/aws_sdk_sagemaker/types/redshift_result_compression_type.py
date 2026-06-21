"""Generated from Smithy shape ``com.amazonaws.sagemaker#RedshiftResultCompressionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The compression used for Redshift query results.</p>"""
RedshiftResultCompressionType: TypeAlias = Literal[
    "None",
    "GZIP",
    "BZIP2",
    "ZSTD",
    "SNAPPY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftResultCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedshiftResultCompressionType:
    return cast(RedshiftResultCompressionType, data)
