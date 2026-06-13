"""Generated from Smithy shape ``com.amazonaws.neptunegraph#PlanCacheType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

PlanCacheType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "AUTO",
    )
)


def serialize_json(value: PlanCacheType) -> str:
    return value


def deserialize_json(data: str) -> PlanCacheType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlanCacheType value: {data!r}")
    return cast(PlanCacheType, data)
