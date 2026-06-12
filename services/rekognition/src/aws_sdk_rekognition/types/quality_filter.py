"""Generated from Smithy shape ``com.amazonaws.rekognition#QualityFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

QualityFilter: TypeAlias = Literal[
    "NONE",
    "AUTO",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "AUTO",
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_aws_json_1_1(value: QualityFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QualityFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QualityFilter value: {data!r}")
    return cast(QualityFilter, data)
