"""Generated from Smithy shape ``com.amazonaws.evs#EnvironmentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

EnvironmentState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "DELETED",
    "CREATE_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "DELETING",
        "DELETED",
        "CREATE_FAILED",
    )
)


def serialize_aws_json_1_0(value: EnvironmentState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnvironmentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentState value: {data!r}")
    return cast(EnvironmentState, data)
