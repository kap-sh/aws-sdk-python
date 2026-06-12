"""Generated from Smithy shape ``com.amazonaws.iotevents#EvaluationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

EvaluationMethod: TypeAlias = Literal[
    "BATCH",
    "SERIAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BATCH",
        "SERIAL",
    )
)


def serialize_json(value: EvaluationMethod) -> str:
    return value


def deserialize_json(data: str) -> EvaluationMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationMethod value: {data!r}")
    return cast(EvaluationMethod, data)
