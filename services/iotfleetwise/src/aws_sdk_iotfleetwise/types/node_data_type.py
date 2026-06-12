"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NodeDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

NodeDataType: TypeAlias = Literal[
    "INT8",
    "UINT8",
    "INT16",
    "UINT16",
    "INT32",
    "UINT32",
    "INT64",
    "UINT64",
    "BOOLEAN",
    "FLOAT",
    "DOUBLE",
    "STRING",
    "UNIX_TIMESTAMP",
    "INT8_ARRAY",
    "UINT8_ARRAY",
    "INT16_ARRAY",
    "UINT16_ARRAY",
    "INT32_ARRAY",
    "UINT32_ARRAY",
    "INT64_ARRAY",
    "UINT64_ARRAY",
    "BOOLEAN_ARRAY",
    "FLOAT_ARRAY",
    "DOUBLE_ARRAY",
    "STRING_ARRAY",
    "UNIX_TIMESTAMP_ARRAY",
    "UNKNOWN",
    "STRUCT",
    "STRUCT_ARRAY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INT8",
        "UINT8",
        "INT16",
        "UINT16",
        "INT32",
        "UINT32",
        "INT64",
        "UINT64",
        "BOOLEAN",
        "FLOAT",
        "DOUBLE",
        "STRING",
        "UNIX_TIMESTAMP",
        "INT8_ARRAY",
        "UINT8_ARRAY",
        "INT16_ARRAY",
        "UINT16_ARRAY",
        "INT32_ARRAY",
        "UINT32_ARRAY",
        "INT64_ARRAY",
        "UINT64_ARRAY",
        "BOOLEAN_ARRAY",
        "FLOAT_ARRAY",
        "DOUBLE_ARRAY",
        "STRING_ARRAY",
        "UNIX_TIMESTAMP_ARRAY",
        "UNKNOWN",
        "STRUCT",
        "STRUCT_ARRAY",
    )
)


def serialize_aws_json_1_0(value: NodeDataType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NodeDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeDataType value: {data!r}")
    return cast(NodeDataType, data)
