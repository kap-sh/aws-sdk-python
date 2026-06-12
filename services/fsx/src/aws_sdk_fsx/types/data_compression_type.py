"""Generated from Smithy shape ``com.amazonaws.fsx#DataCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DataCompressionType: TypeAlias = Literal[
    "NONE",
    "LZ4",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "LZ4",
    )
)


def serialize_aws_json_1_1(value: DataCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataCompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataCompressionType value: {data!r}")
    return cast(DataCompressionType, data)
