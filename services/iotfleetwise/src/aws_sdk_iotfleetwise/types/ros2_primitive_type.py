"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ROS2PrimitiveType``."""

from typing import Literal, TypeAlias, cast

ROS2PrimitiveType: TypeAlias = Literal[
    "BOOL",
    "BYTE",
    "CHAR",
    "FLOAT32",
    "FLOAT64",
    "INT8",
    "UINT8",
    "INT16",
    "UINT16",
    "INT32",
    "UINT32",
    "INT64",
    "UINT64",
    "STRING",
    "WSTRING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ROS2PrimitiveType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ROS2PrimitiveType:
    return cast(ROS2PrimitiveType, data)
