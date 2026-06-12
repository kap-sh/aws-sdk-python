"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_events.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "AUTHORIZED",
        "DEAUTHORIZED",
        "AUTHORIZING",
        "DEAUTHORIZING",
    )
)


def serialize_aws_json_1_1(value: ConnectionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionState value: {data!r}")
    return cast(ConnectionState, data)
