"""Generated from Smithy shape ``com.amazonaws.evs#ConnectorState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

ConnectorState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETING",
        "DELETED",
    )
)


def serialize_aws_json_1_0(value: ConnectorState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectorState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorState value: {data!r}")
    return cast(ConnectorState, data)
