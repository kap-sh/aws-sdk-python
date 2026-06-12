"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloud9.errors import DeserializationError

EnvironmentLifecycleStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "CREATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "CREATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_aws_json_1_1(value: EnvironmentLifecycleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentLifecycleStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EnvironmentLifecycleStatus value: {data!r}"
        )
    return cast(EnvironmentLifecycleStatus, data)
