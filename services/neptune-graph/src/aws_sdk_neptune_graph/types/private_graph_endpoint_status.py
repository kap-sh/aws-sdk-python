"""Generated from Smithy shape ``com.amazonaws.neptunegraph#PrivateGraphEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

PrivateGraphEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: PrivateGraphEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> PrivateGraphEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PrivateGraphEndpointStatus value: {data!r}"
        )
    return cast(PrivateGraphEndpointStatus, data)
