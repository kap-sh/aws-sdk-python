"""Generated from Smithy shape ``com.amazonaws.sagemaker#RedshiftResultCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""<p>The compression used for Redshift query results.</p>"""
RedshiftResultCompressionType: TypeAlias = Literal[
    "None",
    "GZIP",
    "BZIP2",
    "ZSTD",
    "SNAPPY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "GZIP",
        "BZIP2",
        "ZSTD",
        "SNAPPY",
    )
)


def serialize_aws_json_1_1(value: RedshiftResultCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedshiftResultCompressionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RedshiftResultCompressionType value: {data!r}"
        )
    return cast(RedshiftResultCompressionType, data)
