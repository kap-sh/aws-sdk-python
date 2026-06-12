"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

VpcEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_json(value: VpcEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcEndpointStatus value: {data!r}")
    return cast(VpcEndpointStatus, data)
