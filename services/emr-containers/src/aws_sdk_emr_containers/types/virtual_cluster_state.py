"""Generated from Smithy shape ``com.amazonaws.emrcontainers#VirtualClusterState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

VirtualClusterState: TypeAlias = Literal[
    "RUNNING",
    "TERMINATING",
    "TERMINATED",
    "ARRESTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "TERMINATING",
        "TERMINATED",
        "ARRESTED",
    )
)


def serialize_json(value: VirtualClusterState) -> str:
    return value


def deserialize_json(data: str) -> VirtualClusterState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VirtualClusterState value: {data!r}")
    return cast(VirtualClusterState, data)
