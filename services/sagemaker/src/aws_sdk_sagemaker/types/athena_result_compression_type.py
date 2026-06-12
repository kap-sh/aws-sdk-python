"""Generated from Smithy shape ``com.amazonaws.sagemaker#AthenaResultCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""<p>The compression used for Athena query results.</p>"""
AthenaResultCompressionType: TypeAlias = Literal[
    "GZIP",
    "SNAPPY",
    "ZLIB",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GZIP",
        "SNAPPY",
        "ZLIB",
    )
)


def serialize_aws_json_1_1(value: AthenaResultCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AthenaResultCompressionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AthenaResultCompressionType value: {data!r}"
        )
    return cast(AthenaResultCompressionType, data)
