"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StreamExceptionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

StreamExceptionPolicy: TypeAlias = Literal[
    "DROP",
    "CONTINUE",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DROP",
        "CONTINUE",
        "REJECT",
    )
)


def serialize_aws_json_1_0(value: StreamExceptionPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StreamExceptionPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamExceptionPolicy value: {data!r}")
    return cast(StreamExceptionPolicy, data)
