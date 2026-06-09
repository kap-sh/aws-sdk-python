"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonPropagateTags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

DaemonPropagateTags: TypeAlias = Literal[
    "DAEMON",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAEMON",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: DaemonPropagateTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonPropagateTags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DaemonPropagateTags value: {data!r}")
    return cast(DaemonPropagateTags, data)
