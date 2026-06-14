"""Generated from Smithy shape ``com.amazonaws.workspaces#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "PCOIP",
    "WSP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PCOIP",
        "WSP",
    )
)


def serialize_aws_json_1_1(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
