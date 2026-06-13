"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

ServiceFunctionSource: TypeAlias = Literal[
    "AI_GENERATED",
    "USER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AI_GENERATED",
        "USER",
    )
)


def serialize_json(value: ServiceFunctionSource) -> str:
    return value


def deserialize_json(data: str) -> ServiceFunctionSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceFunctionSource value: {data!r}")
    return cast(ServiceFunctionSource, data)
