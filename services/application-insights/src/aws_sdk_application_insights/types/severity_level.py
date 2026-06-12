"""Generated from Smithy shape ``com.amazonaws.applicationinsights#SeverityLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

SeverityLevel: TypeAlias = Literal[
    "Informative",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Informative",
        "Low",
        "Medium",
        "High",
    )
)


def serialize_aws_json_1_1(value: SeverityLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SeverityLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SeverityLevel value: {data!r}")
    return cast(SeverityLevel, data)
