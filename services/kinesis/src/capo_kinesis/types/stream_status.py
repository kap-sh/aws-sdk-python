"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamStatus``."""

from typing import Literal, TypeAlias, cast

StreamStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamStatus:
    return cast(StreamStatus, data)
