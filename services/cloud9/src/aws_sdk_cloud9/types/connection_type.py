"""Generated from Smithy shape ``com.amazonaws.cloud9#ConnectionType``."""

from typing import Literal, TypeAlias, cast

ConnectionType: TypeAlias = Literal[
    "CONNECT_SSH",
    "CONNECT_SSM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionType:
    return cast(ConnectionType, data)
