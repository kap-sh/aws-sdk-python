"""Generated from Smithy shape ``com.amazonaws.wafv2#SensitivityLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

SensitivityLevel: TypeAlias = Literal[
    "LOW",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "HIGH",
    )
)


def serialize_aws_json_1_1(value: SensitivityLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SensitivityLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SensitivityLevel value: {data!r}")
    return cast(SensitivityLevel, data)
