"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupUpdateStrategies``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

NodegroupUpdateStrategies: TypeAlias = Literal[
    "DEFAULT",
    "MINIMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "MINIMAL",
    )
)


def serialize_json(value: NodegroupUpdateStrategies) -> str:
    return value


def deserialize_json(data: str) -> NodegroupUpdateStrategies:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodegroupUpdateStrategies value: {data!r}")
    return cast(NodegroupUpdateStrategies, data)
