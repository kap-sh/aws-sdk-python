"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamMode``."""

from typing import Literal, TypeAlias, cast

StreamMode: TypeAlias = Literal[
    "PROVISIONED",
    "ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamMode:
    return cast(StreamMode, data)
