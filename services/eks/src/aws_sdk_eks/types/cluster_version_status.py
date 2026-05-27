"""Generated from Smithy shape ``com.amazonaws.eks#ClusterVersionStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

ClusterVersionStatus: TypeAlias = Literal[
    "unsupported",
    "standard-support",
    "extended-support",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unsupported",
        "standard-support",
        "extended-support",
    )
)


def serialize_json(value: ClusterVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterVersionStatus value: {data!r}")
    return cast(ClusterVersionStatus, data)
