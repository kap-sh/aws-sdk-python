"""Generated from Smithy shape ``com.amazonaws.batch#ArrayJobDependency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ArrayJobDependency: TypeAlias = Literal[
    "N_TO_N",
    "SEQUENTIAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "N_TO_N",
        "SEQUENTIAL",
    )
)


def serialize_json(value: ArrayJobDependency) -> str:
    return value


def deserialize_json(data: str) -> ArrayJobDependency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArrayJobDependency value: {data!r}")
    return cast(ArrayJobDependency, data)
