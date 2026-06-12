"""Generated from Smithy shape ``com.amazonaws.wafv2#SensitivityToAct``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

SensitivityToAct: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_aws_json_1_1(value: SensitivityToAct) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SensitivityToAct:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SensitivityToAct value: {data!r}")
    return cast(SensitivityToAct, data)
