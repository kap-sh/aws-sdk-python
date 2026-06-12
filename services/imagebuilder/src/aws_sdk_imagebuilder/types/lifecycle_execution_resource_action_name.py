"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourceActionName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecycleExecutionResourceActionName: TypeAlias = Literal[
    "AVAILABLE",
    "DELETE",
    "DEPRECATE",
    "DISABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DELETE",
        "DEPRECATE",
        "DISABLE",
    )
)


def serialize_json(value: LifecycleExecutionResourceActionName) -> str:
    return value


def deserialize_json(data: str) -> LifecycleExecutionResourceActionName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecycleExecutionResourceActionName value: {data!r}"
        )
    return cast(LifecycleExecutionResourceActionName, data)
