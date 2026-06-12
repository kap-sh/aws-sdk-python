"""Generated from Smithy shape ``com.amazonaws.healthlake#ValidationLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

ValidationLevel: TypeAlias = Literal[
    "strict",
    "structure-only",
    "minimal",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "strict",
        "structure-only",
        "minimal",
    )
)


def serialize_aws_json_1_0(value: ValidationLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationLevel value: {data!r}")
    return cast(ValidationLevel, data)
