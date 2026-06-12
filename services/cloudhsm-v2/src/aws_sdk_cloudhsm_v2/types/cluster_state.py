"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ClusterState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm_v2.errors import DeserializationError

ClusterState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "UNINITIALIZED",
    "INITIALIZE_IN_PROGRESS",
    "INITIALIZED",
    "ACTIVE",
    "UPDATE_IN_PROGRESS",
    "MODIFY_IN_PROGRESS",
    "ROLLBACK_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "DELETED",
    "DEGRADED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "UNINITIALIZED",
        "INITIALIZE_IN_PROGRESS",
        "INITIALIZED",
        "ACTIVE",
        "UPDATE_IN_PROGRESS",
        "MODIFY_IN_PROGRESS",
        "ROLLBACK_IN_PROGRESS",
        "DELETE_IN_PROGRESS",
        "DELETED",
        "DEGRADED",
    )
)


def serialize_aws_json_1_1(value: ClusterState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterState value: {data!r}")
    return cast(ClusterState, data)
