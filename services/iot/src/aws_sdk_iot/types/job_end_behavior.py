"""Generated from Smithy shape ``com.amazonaws.iot#JobEndBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

JobEndBehavior: TypeAlias = Literal[
    "STOP_ROLLOUT",
    "CANCEL",
    "FORCE_CANCEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STOP_ROLLOUT",
        "CANCEL",
        "FORCE_CANCEL",
    )
)


def serialize_json(value: JobEndBehavior) -> str:
    return value


def deserialize_json(data: str) -> JobEndBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobEndBehavior value: {data!r}")
    return cast(JobEndBehavior, data)
