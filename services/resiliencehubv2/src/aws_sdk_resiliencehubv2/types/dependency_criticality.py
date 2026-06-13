"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyCriticality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

DependencyCriticality: TypeAlias = Literal[
    "HARD",
    "SOFT",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HARD",
        "SOFT",
        "UNKNOWN",
    )
)


def serialize_json(value: DependencyCriticality) -> str:
    return value


def deserialize_json(data: str) -> DependencyCriticality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DependencyCriticality value: {data!r}")
    return cast(DependencyCriticality, data)
