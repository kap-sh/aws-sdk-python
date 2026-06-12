"""Generated from Smithy shape ``com.amazonaws.glue#DataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DataFormat: TypeAlias = Literal[
    "AVRO",
    "JSON",
    "PROTOBUF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVRO",
        "JSON",
        "PROTOBUF",
    )
)


def serialize_aws_json_1_1(value: DataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataFormat value: {data!r}")
    return cast(DataFormat, data)
