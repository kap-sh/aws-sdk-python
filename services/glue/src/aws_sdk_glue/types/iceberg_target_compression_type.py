"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

IcebergTargetCompressionType: TypeAlias = Literal[
    "gzip",
    "lzo",
    "uncompressed",
    "snappy",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "gzip",
        "lzo",
        "uncompressed",
        "snappy",
    )
)


def serialize_aws_json_1_1(value: IcebergTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergTargetCompressionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IcebergTargetCompressionType value: {data!r}"
        )
    return cast(IcebergTargetCompressionType, data)
