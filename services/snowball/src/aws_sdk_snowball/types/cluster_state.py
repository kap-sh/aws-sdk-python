"""Generated from Smithy shape ``com.amazonaws.snowball#ClusterState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

ClusterState: TypeAlias = Literal[
    "AwaitingQuorum",
    "Pending",
    "InUse",
    "Complete",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AwaitingQuorum",
        "Pending",
        "InUse",
        "Complete",
        "Cancelled",
    )
)


def serialize_aws_json_1_1(value: ClusterState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterState value: {data!r}")
    return cast(ClusterState, data)
