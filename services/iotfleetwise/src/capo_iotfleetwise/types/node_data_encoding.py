"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NodeDataEncoding``."""

from typing import Literal, TypeAlias, cast

NodeDataEncoding: TypeAlias = Literal[
    "BINARY",
    "TYPED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeDataEncoding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NodeDataEncoding:
    return cast(NodeDataEncoding, data)
