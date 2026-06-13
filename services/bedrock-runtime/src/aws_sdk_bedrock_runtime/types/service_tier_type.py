"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ServiceTierType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

ServiceTierType: TypeAlias = Literal[
    "priority",
    "default",
    "flex",
    "reserved",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "priority",
        "default",
        "flex",
        "reserved",
    )
)


def serialize_json(value: ServiceTierType) -> str:
    return value


def deserialize_json(data: str) -> ServiceTierType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceTierType value: {data!r}")
    return cast(ServiceTierType, data)
