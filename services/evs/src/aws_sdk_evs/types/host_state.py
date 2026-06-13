"""Generated from Smithy shape ``com.amazonaws.evs#HostState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

HostState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "UPDATING",
    "DELETING",
    "DELETED",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "UPDATING",
        "DELETING",
        "DELETED",
        "CREATE_FAILED",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_0(value: HostState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HostState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HostState value: {data!r}")
    return cast(HostState, data)
