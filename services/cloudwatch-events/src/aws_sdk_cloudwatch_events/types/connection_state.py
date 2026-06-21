"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionState``."""

from typing import Literal, TypeAlias, cast

ConnectionState: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "AUTHORIZED",
    "DEAUTHORIZED",
    "AUTHORIZING",
    "DEAUTHORIZING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionState:
    return cast(ConnectionState, data)
