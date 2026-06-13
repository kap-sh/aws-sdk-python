"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#CompressionOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

CompressionOption: TypeAlias = Literal[
    "GZIP",
    "PARQUET",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GZIP",
        "PARQUET",
    )
)


def serialize_aws_json_1_1(value: CompressionOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionOption value: {data!r}")
    return cast(CompressionOption, data)
