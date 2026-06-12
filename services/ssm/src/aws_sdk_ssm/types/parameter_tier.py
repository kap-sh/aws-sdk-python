"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ParameterTier: TypeAlias = Literal[
    "Standard",
    "Advanced",
    "Intelligent-Tiering",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "Advanced",
        "Intelligent-Tiering",
    )
)


def serialize_aws_json_1_1(value: ParameterTier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterTier value: {data!r}")
    return cast(ParameterTier, data)
