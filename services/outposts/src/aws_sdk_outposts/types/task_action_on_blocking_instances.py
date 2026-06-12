"""Generated from Smithy shape ``com.amazonaws.outposts#TaskActionOnBlockingInstances``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

TaskActionOnBlockingInstances: TypeAlias = Literal[
    "WAIT_FOR_EVACUATION",
    "FAIL_TASK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WAIT_FOR_EVACUATION",
        "FAIL_TASK",
    )
)


def serialize_json(value: TaskActionOnBlockingInstances) -> str:
    return value


def deserialize_json(data: str) -> TaskActionOnBlockingInstances:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TaskActionOnBlockingInstances value: {data!r}"
        )
    return cast(TaskActionOnBlockingInstances, data)
