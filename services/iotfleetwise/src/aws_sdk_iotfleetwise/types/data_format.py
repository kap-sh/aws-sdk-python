"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

DataFormat: TypeAlias = Literal[
    "JSON",
    "PARQUET",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "PARQUET",
    )
)


def serialize_aws_json_1_0(value: DataFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataFormat value: {data!r}")
    return cast(DataFormat, data)
