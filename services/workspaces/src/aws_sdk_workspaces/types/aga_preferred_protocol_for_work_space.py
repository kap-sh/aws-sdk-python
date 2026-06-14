"""Generated from Smithy shape ``com.amazonaws.workspaces#AGAPreferredProtocolForWorkSpace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

AGAPreferredProtocolForWorkSpace: TypeAlias = Literal[
    "TCP",
    "NONE",
    "INHERITED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TCP",
        "NONE",
        "INHERITED",
    )
)


def serialize_aws_json_1_1(value: AGAPreferredProtocolForWorkSpace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AGAPreferredProtocolForWorkSpace:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AGAPreferredProtocolForWorkSpace value: {data!r}"
        )
    return cast(AGAPreferredProtocolForWorkSpace, data)
