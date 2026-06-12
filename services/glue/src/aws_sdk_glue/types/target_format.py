"""Generated from Smithy shape ``com.amazonaws.glue#TargetFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TargetFormat: TypeAlias = Literal[
    "json",
    "csv",
    "avro",
    "orc",
    "parquet",
    "hudi",
    "delta",
    "iceberg",
    "hyper",
    "xml",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "csv",
        "avro",
        "orc",
        "parquet",
        "hudi",
        "delta",
        "iceberg",
        "hyper",
        "xml",
    )
)


def serialize_aws_json_1_1(value: TargetFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetFormat value: {data!r}")
    return cast(TargetFormat, data)
