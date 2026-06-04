"""Generated from Smithy shape ``com.amazonaws.ecs#BareMetal``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

BareMetal: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "included",
        "required",
        "excluded",
    )
)


def serialize_aws_json_1_1(value: BareMetal) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BareMetal:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BareMetal value: {data!r}")
    return cast(BareMetal, data)
