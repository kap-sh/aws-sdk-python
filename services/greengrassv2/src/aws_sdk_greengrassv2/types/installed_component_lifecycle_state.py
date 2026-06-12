"""Generated from Smithy shape ``com.amazonaws.greengrassv2#InstalledComponentLifecycleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

InstalledComponentLifecycleState: TypeAlias = Literal[
    "NEW",
    "INSTALLED",
    "STARTING",
    "RUNNING",
    "STOPPING",
    "ERRORED",
    "BROKEN",
    "FINISHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "INSTALLED",
        "STARTING",
        "RUNNING",
        "STOPPING",
        "ERRORED",
        "BROKEN",
        "FINISHED",
    )
)


def serialize_json(value: InstalledComponentLifecycleState) -> str:
    return value


def deserialize_json(data: str) -> InstalledComponentLifecycleState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstalledComponentLifecycleState value: {data!r}"
        )
    return cast(InstalledComponentLifecycleState, data)
