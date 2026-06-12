"""Generated from Smithy shape ``com.amazonaws.pi#ContextType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

ContextType: TypeAlias = Literal[
    "CAUSAL",
    "CONTEXTUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAUSAL",
        "CONTEXTUAL",
    )
)


def serialize_aws_json_1_1(value: ContextType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContextType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContextType value: {data!r}")
    return cast(ContextType, data)
