"""Generated from Smithy shape ``com.amazonaws.emr#ClusterState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ClusterState: TypeAlias = Literal[
    "STARTING",
    "BOOTSTRAPPING",
    "RUNNING",
    "WAITING",
    "TERMINATING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "BOOTSTRAPPING",
        "RUNNING",
        "WAITING",
        "TERMINATING",
        "TERMINATED",
        "TERMINATED_WITH_ERRORS",
    )
)


def serialize_aws_json_1_1(value: ClusterState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterState value: {data!r}")
    return cast(ClusterState, data)
