"""Generated from Smithy shape ``com.amazonaws.eks#configStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

configStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "ACTIVE",
    )
)


def serialize_json(value: configStatus) -> str:
    return value


def deserialize_json(data: str) -> configStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown configStatus value: {data!r}")
    return cast(configStatus, data)
