"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadEnvironment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

"""<p>The environment for the workload.</p>"""
WorkloadEnvironment: TypeAlias = Literal[
    "PRODUCTION",
    "PREPRODUCTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRODUCTION",
        "PREPRODUCTION",
    )
)


def serialize_json(value: WorkloadEnvironment) -> str:
    return value


def deserialize_json(data: str) -> WorkloadEnvironment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkloadEnvironment value: {data!r}")
    return cast(WorkloadEnvironment, data)
