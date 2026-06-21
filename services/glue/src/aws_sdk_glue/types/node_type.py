"""Generated from Smithy shape ``com.amazonaws.glue#NodeType``."""

from typing import Literal, TypeAlias, cast

NodeType: TypeAlias = Literal[
    "CRAWLER",
    "JOB",
    "TRIGGER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeType:
    return cast(NodeType, data)
